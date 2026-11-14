"""Text in SVG costumes.

pygame's SVG renderer ignores ``<text>`` elements, but Scratch's paint editor
writes every text a user types as such an element. :func:`add_svg_text` draws
them with ``pygame.font`` onto the bitmap pygame produced for the SVG.

Supported: nested ``<g>`` and ``<text>`` transforms (``translate``, ``scale``,
``rotate``, ``matrix``, ``skew`` is ignored), ``x``/``y``/``dx``/``dy`` on
``<tspan>`` (multi-line text), ``font-size``, ``font-family`` (Scratch's fonts
and common generic names), ``font-weight``, ``font-style``, ``fill`` (names,
``#rgb``, ``#rrggbb``, ``rgb()``, ``none``), ``fill-opacity``, ``opacity``,
``text-anchor``, ``xml:space``, the ``viewBox`` and attributes given as
``style="..."``. Not supported: stroke, gradients, ``textPath``, ``<use>``,
skew, letter spacing, text decoration, clipping.

Nothing here raises: on any problem the plain image is used.
"""
import functools
import math
import os
import re
import xml.etree.ElementTree as ET

import pygame

from pystage.resources import resource_filename

_PROPS = ("fill", "fill-opacity", "opacity", "font-family", "font-size", "font-weight",
          "font-style", "text-anchor", "xml:space", "display", "visibility")
_NUM = re.compile(r"[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?")
_TRANSFORM = re.compile(r"([a-zA-Z]+)\s*\(([^)]*)\)")
_XML_SPACE = "{http://www.w3.org/XML/1998/namespace}space"
_MAX_TEXTS = 500
_MAX_PIXELS = 4096 * 4096


def _local(tag):
    return tag.rsplit("}", 1)[-1] if isinstance(tag, str) else ""


def _numbers(text):
    return [float(n) for n in _NUM.findall(text or "")]


def _length(text, default=0.0):
    """A number with an optional unit (px, pt ...), in user units."""
    m = _NUM.match((text or "").strip())
    if not m:
        return default
    value = float(m.group())
    unit = (text or "").strip()[m.end():].strip()
    return value * {"pt": 4 / 3, "pc": 16, "mm": 96 / 25.4, "cm": 96 / 2.54, "in": 96}.get(unit, 1)


# Matrices are tuples (a, b, c, d, e, f): x' = a*x + c*y + e, y' = b*x + d*y + f
_IDENTITY = (1.0, 0.0, 0.0, 1.0, 0.0, 0.0)


def _multiply(m, n):
    """The matrix applying n first, then m."""
    return (m[0] * n[0] + m[2] * n[1], m[1] * n[0] + m[3] * n[1],
            m[0] * n[2] + m[2] * n[3], m[1] * n[2] + m[3] * n[3],
            m[0] * n[4] + m[2] * n[5] + m[4], m[1] * n[4] + m[3] * n[5] + m[5])


def parse_transform(text):
    result = _IDENTITY
    for name, args in _TRANSFORM.findall(text or ""):
        v = _numbers(args)
        name = name.lower()
        if name == "translate" and v:
            m = (1, 0, 0, 1, v[0], v[1] if len(v) > 1 else 0)
        elif name == "scale" and v:
            m = (v[0], 0, 0, v[1] if len(v) > 1 else v[0], 0, 0)
        elif name == "rotate" and v:
            c, s = math.cos(math.radians(v[0])), math.sin(math.radians(v[0]))
            m = (c, s, -s, c, 0, 0)
            if len(v) >= 3:
                m = _multiply(_multiply((1, 0, 0, 1, v[1], v[2]), m), (1, 0, 0, 1, -v[1], -v[2]))
        elif name == "matrix" and len(v) >= 6:
            m = tuple(v[:6])
        else:
            continue
        result = _multiply(result, m)
    return result


def parse_color(value):
    """(r, g, b) or None for ``none`` and anything unknown."""
    value = (value or "").strip()
    if not value or value.lower() in ("none", "transparent"):
        return None
    try:
        if value.lower().startswith("rgb"):
            nums = _numbers(value)[:3]
            if len(nums) < 3:
                return None
            if "%" in value:
                nums = [n * 2.55 for n in nums]
            return tuple(max(0, min(255, round(n))) for n in nums)
        if re.fullmatch(r"#[0-9a-fA-F]{3}", value):
            value = "#" + "".join(ch * 2 for ch in value[1:])
        c = pygame.Color(value)
        return c.r, c.g, c.b
    except (ValueError, TypeError):
        return None


def _style(element):
    props = {}
    for name in _PROPS:
        if element.get(name) is not None:
            props[name] = element.get(name)
    if element.get(_XML_SPACE) is not None:
        props["xml:space"] = element.get(_XML_SPACE)
    for declaration in (element.get("style") or "").split(";"):
        if ":" in declaration:
            key, val = declaration.split(":", 1)
            if key.strip() in _PROPS:
                props[key.strip()] = val.strip()
    return props


##
# Fonts
#

# Scratch's font families (scratch-paint) and the original font files that
# Scratch ships (scratch-render-fonts), bundled in fonts/scratch. Scratch only
# has the regular weight, there is no bold or italic cut.
_SCRATCH_FONTS = {
    "sans serif": "NotoSans-Medium.ttf",
    "serif": "SourceSerifPro-Regular.otf",
    "handwriting": "Handlee-Regular.ttf",
    "marker": "Knewave.ttf",
    "curly": "Griffy-Regular.ttf",
    "pixel": "Grand9K-Pixel.ttf",
}
# Scratch 2 names, converted by scratch-svg-renderer when the whole attribute is one of them
_SCRATCH2_NAMES = {"helvetica": "sans serif", "mystery": "curly", "gloria": "handwriting", "donegal": "serif"}

# Families without a bundled font (Chinese, Japanese and Korean: Scratch uses
# system fonts as well; Pixel only if its file is missing) and generic names,
# with system fonts that look similar and the bundled Roboto to use if there is none.
_FAMILIES = {
    "pixel": (["couriernew", "courier", "dejavusansmono", "liberationmono"], "regular"),
    "monospace": (["couriernew", "courier", "dejavusansmono", "liberationmono"], "regular"),
    "sans-serif": (["helvetica", "arial", "dejavusans", "liberationsans", "freesans"], "regular"),
    "chinese": (["pingfangsc", "heitisc", "microsoftyahei", "notosanscjksc", "notosanssc", "simsun", "arialunicodems"], "regular"),
    "japanese": (["hiraginosans", "hiraginokakugothicpro", "meiryo", "notosanscjkjp", "notosansjp", "msgothic", "arialunicodems"], "regular"),
    "korean": (["applesdgothicneo", "malgungothic", "notosanskr", "notosanscjkkr", "arialunicodems"], "regular"),
}
_FALLBACK_FILES = {"regular": "roboto-regular.ttf", "bold": "roboto-bold.ttf", "light": "roboto-light.ttf"}


def _scratch_font(name):
    """The path of the bundled Scratch font of a (lower case) family name or None."""
    filename = _SCRATCH_FONTS.get(name)
    if filename:
        path = resource_filename("fonts/scratch/" + filename)
        if os.path.isfile(path):
            return path
    return None


@functools.lru_cache(maxsize=None)
def _font_file(family, bold, italic):
    """The file of a font for a family list (comma separated), never None.

    Scratch's own families use the bundled originals, other names a similar
    system font, and Roboto is the last resort."""
    fallback = "regular"
    family = (family or "").strip().strip("'\"").strip().lower()
    if not family:
        family = "sans serif"
    family = _SCRATCH2_NAMES.get(family, family)
    for name in family.split(","):
        name = name.strip().strip("'\"").lower()
        if not name:
            continue
        path = _scratch_font(name)
        if path:
            return path
        candidates, fb = _FAMILIES.get(name, ([re.sub(r"[^a-z0-9]", "", name)], "regular"))
        if name in _FAMILIES:
            fallback = fb
        for candidate in candidates:
            try:
                path = pygame.font.match_font(candidate, bold=bold, italic=italic)
            except Exception:
                path = None
            if path:
                return path
        if name in _FAMILIES:
            break
    if bold:
        fallback = "bold"
    return resource_filename("fonts/" + _FALLBACK_FILES[fallback])


@functools.lru_cache(maxsize=256)
def _font(path, size):
    return pygame.font.Font(path, size)


def _is_bold(weight):
    weight = (weight or "").strip().lower()
    if weight in ("bold", "bolder"):
        return True
    return weight.isdigit() and int(weight) >= 600


##
# Collecting the text
#

class _Run:
    def __init__(self, text, x, y, props):
        self.text, self.x, self.y, self.props = text, x, y, props


def _collapse(text, preserve):
    if preserve:
        return text.replace("\n", " ").replace("\t", " ")
    return re.sub(r"\s+", " ", text)


def _runs(text_element, props):
    """The runs of one ``<text>``: pieces of text with their start position
    in the local coordinates of the element (the baseline is at y)."""
    runs = []
    state = {"x": _numbers(text_element.get("x"))[:1] or [0.0], "y": _numbers(text_element.get("y"))[:1] or [0.0]}
    pen = [state["x"][0], state["y"][0]]

    def add(text, p):
        if not text:
            return
        text = _collapse(text, p.get("xml:space") == "preserve")
        runs.append(_Run(text, pen[0], pen[1], p))
        pen[0] += _text_width(text, p)

    def walk(element, p):
        add(element.text, p)
        for child in element:
            if _local(child.tag) == "tspan":
                cp = dict(p)
                cp.update(_style(child))
                if child.get("x") is not None:
                    pen[0] = (_numbers(child.get("x")) or [pen[0]])[0]
                if child.get("y") is not None:
                    pen[1] = (_numbers(child.get("y")) or [pen[1]])[0]
                pen[0] += (_numbers(child.get("dx")) or [0])[0]
                pen[1] += (_numbers(child.get("dy")) or [0])[0]
                walk(child, cp)
            add(child.tail, p)

    walk(text_element, props)
    return runs


def _text_width(text, props):
    try:
        size = max(1, round(_length(props.get("font-size"), 16)))
        return _font(_font_file(props.get("font-family"), _is_bold(props.get("font-weight")),
                                (props.get("font-style") or "").lower() in ("italic", "oblique")), size).size(text)[0]
    except Exception:
        return 0


def _collect(element, matrix, props, out):
    """Depth first: appends (text element, its matrix, its properties)."""
    if len(out) >= _MAX_TEXTS:
        return
    tag = _local(element.tag)
    if tag in ("defs", "clipPath", "mask", "symbol", "metadata", "style", "title", "desc"):
        return
    props = {**props, **_style(element)}
    if props.get("display") == "none" or props.get("visibility") == "hidden":
        return
    matrix = _multiply(matrix, parse_transform(element.get("transform")))
    if tag == "text":
        out.append((element, matrix, props))
        return
    for child in element:
        _collect(child, matrix, props, out)


##
# Rendering
#

# One font size is rendered at most this large, whatever the transform says.
_MAX_FONT_PX = 1000


def _render_run(run, matrix, to_px):
    """Render one run: (surface, topleft) in bitmap pixels or None."""
    props = run.props
    color = parse_color(props.get("fill", "black"))
    if color is None:
        return None
    try:
        opacity = float(props.get("fill-opacity", 1)) * float(props.get("opacity", 1))
    except ValueError:
        opacity = 1.0
    opacity = max(0.0, min(1.0, opacity))
    if opacity == 0 or not run.text.strip():
        return None
    m = _multiply(to_px, matrix)
    scale_x, scale_y = math.hypot(m[0], m[1]), math.hypot(m[2], m[3])
    size = _length(props.get("font-size"), 16)
    px = size * scale_y
    if px < 1 or scale_x == 0 or px > _MAX_FONT_PX:
        return None
    bold = _is_bold(props.get("font-weight"))
    italic = (props.get("font-style") or "").lower() in ("italic", "oblique")
    font = _font(_font_file(props.get("font-family"), bold, italic), max(1, round(px)))
    surface = font.render(run.text, True, color)
    if opacity < 1:
        surface.fill((255, 255, 255, round(opacity * 255)), special_flags=pygame.BLEND_RGBA_MULT)
    # Keep the width exact when the transform is not uniform
    stretch = scale_x / scale_y
    if abs(stretch - 1) > 0.02:
        surface = pygame.transform.smoothscale(surface, (max(1, round(surface.get_width() * stretch)), surface.get_height()))
    x, y = run.x, run.y
    anchor = props.get("text-anchor", "start")
    width_local = font.size(run.text)[0] * stretch / scale_x if scale_x else 0
    # anchor relative to the run: shift in local units along the text direction
    if anchor == "middle":
        x -= width_local / 2
    elif anchor == "end":
        x -= width_local
    ox, oy = m[0] * x + m[2] * y + m[4], m[1] * x + m[3] * y + m[5]
    baseline = font.get_ascent()
    angle = -math.degrees(math.atan2(m[1], m[0]))
    if abs(angle) > 0.5:
        w, h = surface.get_size()
        # vector from the surface centre to the start of the baseline
        v = pygame.Vector2(-w / 2, baseline - h / 2)
        surface = pygame.transform.rotate(surface, angle)
        # pygame rotates counter-clockwise, y points down
        v = v.rotate(-angle)
        centre = pygame.Vector2(ox, oy) - v
        topleft = (centre.x - surface.get_width() / 2, centre.y - surface.get_height() / 2)
    else:
        topleft = (ox, oy - baseline)
    return surface, (round(topleft[0]), round(topleft[1]))


def add_svg_text(image, filename):
    """Draw the text of the SVG ``filename`` onto ``image`` (what pygame
    loaded from it). Returns ``(image, (pad_x, pad_y))``: the image, enlarged
    if the text reaches over its border, and how far the old origin moved."""
    try:
        with open(filename, "rb") as f:
            data = f.read(20_000_000)
        if b"<text" not in data:
            return image, (0, 0)
        root = ET.fromstring(data)
        if _local(root.tag) != "svg":
            return image, (0, 0)
        w, h = image.get_size()
        view = _numbers(root.get("viewBox"))
        if len(view) == 4 and view[2] > 0 and view[3] > 0:
            vx, vy, vw, vh = view
        else:
            vx, vy = 0.0, 0.0
            vw = _length(root.get("width"), w) or w
            vh = _length(root.get("height"), h) or h
        # pygame rounds the size of the bitmap up
        sx, sy = w / vw, h / vh
        to_px = (sx, 0.0, 0.0, sy, -vx * sx, -vy * sy)

        texts = []
        _collect(root, _IDENTITY, {"fill": "black", "font-size": "16", "font-family": "Sans Serif"}, texts)
        parts = []
        for element, matrix, props in texts:
            for run in _runs(element, props):
                rendered = _render_run(run, matrix, to_px)
                if rendered is not None:
                    parts.append(rendered)
        if not parts:
            return image, (0, 0)
        # only the ink counts: the empty space above and below a line (ascent,
        # descent) must not enlarge the image
        inks = []
        for surface, (x, y) in parts:
            ink = surface.get_bounding_rect()
            if ink.width and ink.height:
                inks.append(pygame.Rect(x + ink.x, y + ink.y, ink.width, ink.height))
        if not inks:
            return image, (0, 0)
        left = min(0, *(r.left for r in inks))
        top = min(0, *(r.top for r in inks))
        right = max(w, *(r.right for r in inks))
        bottom = max(h, *(r.bottom for r in inks))
        if (right - left) * (bottom - top) > _MAX_PIXELS:
            return image, (0, 0)
        result = pygame.Surface((right - left, bottom - top), pygame.SRCALPHA)
        result.blit(image, (-left, -top))
        for surface, (x, y) in parts:
            result.blit(surface, (x - left, y - top))
        return result, (-left, -top)
    except Exception:
        return image, (0, 0)

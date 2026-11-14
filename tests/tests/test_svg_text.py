"""Text in SVG costumes: pygame ignores <text>, pystage draws it."""
import pygame
import pytest

from pystage.en import Stage

HEAD = '<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0,0,{w},{h}">'


def svg(body, w=200, h=60):
    return HEAD.format(w=w, h=h) + body + "</svg>"


def text(content, transform="translate(10,40)", extra=""):
    return (f'<text transform="{transform}" font-size="40" font-family="Sans Serif" fill="#ff0000" '
            f'xml:space="preserve" {extra}><tspan x="0" dy="0">{content}</tspan></text>')


def costume_image(tmp_path, content, name="c"):
    path = tmp_path / f"{name}.svg"
    path.write_text(content)
    stage = Stage()
    sprite = stage.add_a_sprite()
    sprite._core.pystage_addcostume(str(path))
    return stage, sprite, sprite._core.costume_manager.costumes[-1]


def red_rect(image):
    """Bounding rectangle of the red pixels."""
    mask = pygame.mask.from_threshold(image, (255, 0, 0, 255), (30, 30, 30, 255))
    rects = mask.get_bounding_rects()
    # the costume is cropped, the offset is where it was in the original image
    return rects[0].unionall(rects[1:]).move(image.get_offset()) if rects else None


def test_text_only_is_visible_and_clickable(tmp_path):
    stage, sprite, costume = costume_image(tmp_path, svg(text("Hello")))
    assert costume.image.get_bounding_rect().width > 20
    core = sprite._core
    core.costume_manager.update_sprite_image()
    # a pixel of the text is clickable: find one
    mask = pygame.mask.from_surface(core.image)
    x, y = next((x, y) for x in range(core.image.get_width()) for y in range(core.image.get_height()) if mask.get_at((x, y)))
    pos = (core.rect.left + x, core.rect.top + y)
    assert stage._core._sprite_at(pos, [core]) is core


def test_text_lands_inside_the_shape(tmp_path):
    body = '<rect x="0" y="0" width="200" height="60" fill="#0000ff"/>' + text("PLAY", "translate(70,40) scale(0.5,0.5)")
    _, _, costume = costume_image(tmp_path, svg(body))
    assert costume.image.get_size() == (200, 60)
    rect = red_rect(costume.image)
    assert rect is not None
    # the text is at x=70..~110, baseline y=40 and 20 px high
    assert 65 <= rect.left <= 80 and rect.right <= 130
    assert 15 <= rect.top and rect.bottom <= 45


def test_nested_group_transforms(tmp_path):
    body = ('<g transform="translate(-50,-20)"><g transform="translate(60,20)">'
            + text("X", "translate(20,40)") + "</g></g>")
    _, _, costume = costume_image(tmp_path, svg(body))
    rect = red_rect(costume.image)
    # x: -50 + 60 + 20 = 30
    assert rect is not None and 28 <= rect.left <= 40 and rect.bottom <= 62


def test_viewbox_offset(tmp_path):
    content = ('<svg xmlns="http://www.w3.org/2000/svg" width="200" height="60" viewBox="100,50,200,60">'
               + text("X", "translate(110,90)") + "</svg>")
    _, _, costume = costume_image(tmp_path, content)
    rect = red_rect(costume.image)
    assert rect is not None and rect.left < 25 and rect.bottom <= 42


def test_multiline(tmp_path):
    one = costume_image(tmp_path, svg(text("A")), "one")[2]
    body = ('<text font-size="30" fill="#ff0000" font-family="Sans Serif" transform="translate(10,30)">'
            '<tspan x="0" dy="0">A</tspan><tspan x="0" dy="30">B</tspan></text>')
    _, _, two = costume_image(tmp_path, svg(body, h=80), "two")
    assert two.image.get_height() > 35 and two.image.get_height() > one.image.get_height() * 0.5
    rect = red_rect(two.image)
    assert rect.height > 35


def test_colors_and_opacity(tmp_path):
    for fill, expected in (("red", (255, 0, 0)), ("#f00", (255, 0, 0)), ("rgb(255,0,0)", (255, 0, 0))):
        body = f'<text x="5" y="40" font-size="40" fill="{fill}">W</text>'
        image = costume_image(tmp_path, svg(body), "c" + fill.strip("#()").replace(",", ""))[2].image
        assert red_rect(image) is not None
    # fill none draws nothing: the costume stays invisible (1x1)
    none = costume_image(tmp_path, svg('<text x="5" y="40" font-size="40" fill="none">W</text>'), "none")[2]
    assert none.image.get_bounding_rect().width <= 1
    half = costume_image(tmp_path, svg('<text x="5" y="40" font-size="40" fill="#ff0000" fill-opacity="0.5">W</text>'), "half")[2]
    alphas = {half.image.get_at((x, y)).a for x in range(half.image.get_width()) for y in range(half.image.get_height())}
    assert max(alphas) <= 130 and max(alphas) > 60


def test_text_anchor_middle(tmp_path):
    body = text("WW", "translate(100,40)", 'text-anchor="middle"')
    rect = red_rect(costume_image(tmp_path, svg(body), "mid")[2].image)
    assert abs((rect.left + rect.right) / 2 - 100) < 10


def test_text_outside_grows_surface_and_keeps_centre(tmp_path):
    # the shape is 40x40, the text reaches to the right and to the left of it
    body = '<rect x="0" y="0" width="40" height="40" fill="#0000ff"/>' + text("Wide text", "translate(-30,40)")
    _, _, costume = costume_image(tmp_path, svg(body, 40, 40))
    assert costume.image.get_width() > 100
    # the centre of the shape (20, 20) is still the centre of the shape in the image
    blue = pygame.mask.from_threshold(costume.image, (0, 0, 255, 255), (10, 10, 10, 255)).get_bounding_rects()[0]
    assert abs(costume.center_x - blue.centerx) <= 1 and abs(costume.center_y - blue.centery) <= 1


def test_rotated_text(tmp_path):
    body = text("WWWW", "translate(100,50) rotate(-90)")
    rect = red_rect(costume_image(tmp_path, svg(body, 200, 100), "rot")[2].image)
    assert rect.height > rect.width


@pytest.mark.parametrize("content", [
    "<svg", "not xml at all <text>", svg('<text font-size="abc" x="q" fill="###">a<tspan dy="x">b</tspan></text>'),
    svg('<text transform="matrix(0,0,0,0,0,0)">a</text>'), svg('<text transform="scale(1e9)" font-size="40">a</text>'),
    svg('<text font-size="-5">a</text>'), svg('<text/>'),
])
def test_malformed_never_raises(tmp_path, content):
    stage, sprite, costume = costume_image(tmp_path, content, "bad")
    stage._core._frame(1 / 60)
    assert costume.image.get_width() >= 1


def test_svg_without_text_is_unchanged(tmp_path):
    _, _, costume = costume_image(tmp_path, svg('<rect width="50" height="20" fill="#00ff00"/>'))
    assert costume.image.get_size() == (50, 20)


def test_svg_warning_only_once(tmp_path, capsys):
    import pystage.core.assets as assets
    assets._svg_notice_shown = False
    costume_image(tmp_path, svg(text("A")), "w1")
    costume_image(tmp_path, svg(text("B")), "w2")
    assert capsys.readouterr().out.count("SVG") == 1


SCRATCH_FONTS = {
    "Sans Serif": "NotoSans-Medium.ttf",
    "Serif": "SourceSerifPro-Regular.otf",
    "Handwriting": "Handlee-Regular.ttf",
    "Marker": "Knewave.ttf",
    "Curly": "Griffy-Regular.ttf",
}


@pytest.mark.parametrize("family,filename", SCRATCH_FONTS.items())
def test_scratch_families_use_bundled_fonts(family, filename):
    import os
    from pystage.core import svg_text
    path = svg_text._font_file(family, False, False)
    assert os.path.basename(path) == filename
    assert os.path.dirname(path).endswith(os.path.join("fonts", "scratch"))
    assert os.path.isfile(path)
    surface = svg_text._font(path, 40).render("Hello", True, (255, 255, 255))
    assert surface.get_bounding_rect().width > 20


def test_bundled_fonts_ship_with_licences():
    import os
    from pystage.resources import resource_filename
    folder = resource_filename("fonts/scratch")
    names = os.listdir(os.path.join(folder, "licenses"))
    assert len([n for n in names if n.startswith("OFL-")]) == len(SCRATCH_FONTS)
    assert os.path.isfile(os.path.join(folder, "README.md"))


def test_font_family_aliases_and_fallbacks():
    import os
    from pystage.core import svg_text
    name = lambda family, bold=False: os.path.basename(svg_text._font_file(family, bold, False))
    assert name(None) == name("") == "NotoSans-Medium.ttf"
    assert name("Helvetica") == "NotoSans-Medium.ttf"
    assert name("Gloria") == "Handlee-Regular.ttf"
    assert name("'Sans Serif', Arial") == "NotoSans-Medium.ttf"
    # unknown families and bold fall back to Roboto (or a system font), never fail
    assert os.path.isfile(svg_text._font_file("No Such Font 123", False, False))
    assert name("No Such Font 123", True) == "roboto-bold.ttf"

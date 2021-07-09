---
jupyter:
  jupytext:
    formats: md,ipynb
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.7.1
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from time import sleep
import requests
import os
import re 
from IPython.display import SVG, display
import xml.etree.ElementTree as ET
import copy
from pathlib import Path
import json
import time
import base64

not_letters = re.compile(r"[^a-zA-Z0-9]")
namespaces = {"svg": "http://www.w3.org/2000/svg", "xlink": "http://www.w3.org/1999/xlink" }
# Scratch icons:
icons = ["repeat.svg", "dropdown-arrow.svg", "rotate-left.svg", "rotate-right.svg", "green-flag.svg"]

```

```python
def get_scratch_icons():
    for i in icons:
        data = requests.get(f"https://scratch.mit.edu/static/blocks-media/{i}").text
        with open(f"icons/{i}", "w", encoding="utf-8") as f:
            f.write(data)
```

```python
def start_selenium():
    options = Options()
    #options.add_argument('--headless')
    # use to set language via browser
    profile = webdriver.FirefoxProfile()
    #profile.set_preference('intl.accept_languages', "de")
    driver = webdriver.Firefox(options=options, firefox_profile=profile)
    driver.set_window_size(1024, 768)
    driver.get("https://scratch.mit.edu/projects/editor/")
    time.sleep(3)
    return driver
    
```

```python
def switch_language(driver: webdriver.Firefox, language: str):
    select : Select = Select(driver.find_element_by_css_selector(".language-selector_language-select_8Vfnm"))
    select.select_by_value(language)
    driver.language = language
    time.sleep(1)
```

```python
def activate_extension(driver: webdriver.Firefox, name : str):
    language = None
    if hasattr(driver, "language"):
        language = driver.language
    switch_language(driver, "en")
    button = driver.find_element_by_class_name("gui_extension-button_2T7PA")
    button.click()
    time.sleep(1)
    ext = driver.find_element_by_xpath(f'//span[text()="{name.capitalize()}"]')
    ext.click()
    time.sleep(1)
    if language:
        switch_language(driver, language)
```

```python
def scrape_blocks(driver, language="en"):
    #profile.set_preference('intl.accept_languages', language)
    switch_language(driver, language)
    box = driver.find_element_by_class_name("blocklyFlyout")
    svg = box.get_attribute("outerHTML")
    return svg

```

```python
def fix_svg_and_get_opcodes(svg):
    # adjust path to icons
    svg = svg.replace("/static/blocks-media/", "icons/")
    # create a full xml document
    entities = '<!ENTITY quot "&#34;">  <!ENTITY amp "&#38;">  <!ENTITY apos "&#39;">  <!ENTITY lt "&#60;">  <!ENTITY gt "&#62;">  <!ENTITY nbsp "&#160;">  <!ENTITY iexcl "&#161;">  <!ENTITY cent "&#162;">  <!ENTITY pound "&#163;">  <!ENTITY curren "&#164;">  <!ENTITY yen "&#165;">  <!ENTITY brvbar "&#166;">  <!ENTITY sect "&#167;">  <!ENTITY uml "&#168;">  <!ENTITY copy "&#169;">  <!ENTITY ordf "&#170;">  <!ENTITY laquo "&#171;">  <!ENTITY not "&#172;">  <!ENTITY shy "&#173;">  <!ENTITY reg "&#174;">  <!ENTITY macr "&#175;">  <!ENTITY deg "&#176;">  <!ENTITY plusmn "&#177;">  <!ENTITY sup2 "&#178;">  <!ENTITY sup3 "&#179;">  <!ENTITY acute "&#180;">  <!ENTITY micro "&#181;">  <!ENTITY para "&#182;">  <!ENTITY middot "&#183;">  <!ENTITY cedil "&#184;">  <!ENTITY sup1 "&#185;">  <!ENTITY ordm "&#186;">  <!ENTITY raquo "&#187;">  <!ENTITY frac14 "&#188;">  <!ENTITY frac12 "&#189;">  <!ENTITY frac34 "&#190;">  <!ENTITY iquest "&#191;">  <!ENTITY Agrave "&#192;">  <!ENTITY Aacute "&#193;">  <!ENTITY Acirc "&#194;">  <!ENTITY Atilde "&#195;">  <!ENTITY Auml "&#196;">  <!ENTITY Aring "&#197;">  <!ENTITY AElig "&#198;">  <!ENTITY Ccedil "&#199;">  <!ENTITY Egrave "&#200;">  <!ENTITY Eacute "&#201;">  <!ENTITY Ecirc "&#202;">  <!ENTITY Euml "&#203;">  <!ENTITY Igrave "&#204;">  <!ENTITY Iacute "&#205;">  <!ENTITY Icirc "&#206;">  <!ENTITY Iuml "&#207;">  <!ENTITY ETH "&#208;">  <!ENTITY Ntilde "&#209;">  <!ENTITY Ograve "&#210;">  <!ENTITY Oacute "&#211;">  <!ENTITY Ocirc "&#212;">  <!ENTITY Otilde "&#213;">  <!ENTITY Ouml "&#214;">  <!ENTITY times "&#215;">  <!ENTITY Oslash "&#216;">  <!ENTITY Ugrave "&#217;">  <!ENTITY Uacute "&#218;">  <!ENTITY Ucirc "&#219;">  <!ENTITY Uuml "&#220;">  <!ENTITY Yacute "&#221;">  <!ENTITY THORN "&#222;">  <!ENTITY szlig "&#223;">  <!ENTITY agrave "&#224;">  <!ENTITY aacute "&#225;">  <!ENTITY acirc "&#226;">  <!ENTITY atilde "&#227;">  <!ENTITY auml "&#228;">  <!ENTITY aring "&#229;">  <!ENTITY aelig "&#230;">  <!ENTITY ccedil "&#231;">  <!ENTITY egrave "&#232;">  <!ENTITY eacute "&#233;">  <!ENTITY ecirc "&#234;">  <!ENTITY euml "&#235;">  <!ENTITY igrave "&#236;">  <!ENTITY iacute "&#237;">  <!ENTITY icirc "&#238;">  <!ENTITY iuml "&#239;">  <!ENTITY eth "&#240;">  <!ENTITY ntilde "&#241;">  <!ENTITY ograve "&#242;">  <!ENTITY oacute "&#243;">  <!ENTITY ocirc "&#244;">  <!ENTITY otilde "&#245;">  <!ENTITY ouml "&#246;">  <!ENTITY divide "&#247;">  <!ENTITY oslash "&#248;">  <!ENTITY ugrave "&#249;">  <!ENTITY uacute "&#250;">  <!ENTITY ucirc "&#251;">  <!ENTITY uuml "&#252;">  <!ENTITY yacute "&#253;">  <!ENTITY thorn "&#254;">  <!ENTITY yuml "&#255;">  <!ENTITY OElig "&#338;">  <!ENTITY oelig "&#339;">  <!ENTITY Scaron "&#352;">  <!ENTITY scaron "&#353;">  <!ENTITY Yuml "&#376;">  <!ENTITY fnof "&#402;">  <!ENTITY circ "&#710;">  <!ENTITY tilde "&#732;">  <!ENTITY Alpha "&#913;">  <!ENTITY Beta "&#914;">  <!ENTITY Gamma "&#915;">  <!ENTITY Delta "&#916;">  <!ENTITY Epsilon "&#917;">  <!ENTITY Zeta "&#918;">  <!ENTITY Eta "&#919;">  <!ENTITY Theta "&#920;">  <!ENTITY Iota "&#921;">  <!ENTITY Kappa "&#922;">  <!ENTITY Lambda "&#923;">  <!ENTITY Mu "&#924;">  <!ENTITY Nu "&#925;">  <!ENTITY Xi "&#926;">  <!ENTITY Omicron "&#927;">  <!ENTITY Pi "&#928;">  <!ENTITY Rho "&#929;">  <!ENTITY Sigma "&#931;">  <!ENTITY Tau "&#932;">  <!ENTITY Upsilon "&#933;">  <!ENTITY Phi "&#934;">  <!ENTITY Chi "&#935;">  <!ENTITY Psi "&#936;">  <!ENTITY Omega "&#937;">  <!ENTITY alpha "&#945;">  <!ENTITY beta "&#946;">  <!ENTITY gamma "&#947;">  <!ENTITY delta "&#948;">  <!ENTITY epsilon "&#949;">  <!ENTITY zeta "&#950;">  <!ENTITY eta "&#951;">  <!ENTITY theta "&#952;">  <!ENTITY iota "&#953;">  <!ENTITY kappa "&#954;">  <!ENTITY lambda "&#955;">  <!ENTITY mu "&#956;">  <!ENTITY nu "&#957;">  <!ENTITY xi "&#958;">  <!ENTITY omicron "&#959;">  <!ENTITY pi "&#960;">  <!ENTITY rho "&#961;">  <!ENTITY sigmaf "&#962;">  <!ENTITY sigma "&#963;">  <!ENTITY tau "&#964;">  <!ENTITY upsilon "&#965;">  <!ENTITY phi "&#966;">  <!ENTITY chi "&#967;">  <!ENTITY psi "&#968;">  <!ENTITY omega "&#969;">  <!ENTITY thetasym "&#977;">  <!ENTITY upsih "&#978;">  <!ENTITY piv "&#982;">  <!ENTITY ensp "&#8194;">  <!ENTITY emsp "&#8195;">  <!ENTITY thinsp "&#8201;">  <!ENTITY zwnj "&#8204;">  <!ENTITY zwj "&#8205;">  <!ENTITY lrm "&#8206;">  <!ENTITY rlm "&#8207;">  <!ENTITY ndash "&#8211;">  <!ENTITY mdash "&#8212;">  <!ENTITY lsquo "&#8216;">  <!ENTITY rsquo "&#8217;">  <!ENTITY sbquo "&#8218;">  <!ENTITY ldquo "&#8220;">  <!ENTITY rdquo "&#8221;">  <!ENTITY bdquo "&#8222;">  <!ENTITY dagger "&#8224;">  <!ENTITY Dagger "&#8225;">  <!ENTITY bull "&#8226;">  <!ENTITY hellip "&#8230;">  <!ENTITY permil "&#8240;">  <!ENTITY prime "&#8242;">  <!ENTITY Prime "&#8243;">  <!ENTITY lsaquo "&#8249;">  <!ENTITY rsaquo "&#8250;">  <!ENTITY oline "&#8254;">  <!ENTITY frasl "&#8260;">  <!ENTITY euro "&#8364;">  <!ENTITY image "&#8465;">  <!ENTITY weierp "&#8472;">  <!ENTITY real "&#8476;">  <!ENTITY trade "&#8482;">  <!ENTITY alefsym "&#8501;">  <!ENTITY larr "&#8592;">  <!ENTITY uarr "&#8593;">  <!ENTITY rarr "&#8594;">  <!ENTITY darr "&#8595;">  <!ENTITY harr "&#8596;">  <!ENTITY crarr "&#8629;">  <!ENTITY lArr "&#8656;">  <!ENTITY uArr "&#8657;">  <!ENTITY rArr "&#8658;">  <!ENTITY dArr "&#8659;">  <!ENTITY hArr "&#8660;">  <!ENTITY forall "&#8704;">  <!ENTITY part "&#8706;">  <!ENTITY exist "&#8707;">  <!ENTITY empty "&#8709;">  <!ENTITY nabla "&#8711;">  <!ENTITY isin "&#8712;">  <!ENTITY notin "&#8713;">  <!ENTITY ni "&#8715;">  <!ENTITY prod "&#8719;">  <!ENTITY sum "&#8721;">  <!ENTITY minus "&#8722;">  <!ENTITY lowast "&#8727;">  <!ENTITY radic "&#8730;">  <!ENTITY prop "&#8733;">  <!ENTITY infin "&#8734;">  <!ENTITY ang "&#8736;">  <!ENTITY and "&#8743;">  <!ENTITY or "&#8744;">  <!ENTITY cap "&#8745;">  <!ENTITY cup "&#8746;">  <!ENTITY int "&#8747;">  <!ENTITY there4 "&#8756;">  <!ENTITY sim "&#8764;">  <!ENTITY cong "&#8773;">  <!ENTITY asymp "&#8776;">  <!ENTITY ne "&#8800;">  <!ENTITY equiv "&#8801;">  <!ENTITY le "&#8804;">  <!ENTITY ge "&#8805;">  <!ENTITY sub "&#8834;">  <!ENTITY sup "&#8835;">  <!ENTITY nsub "&#8836;">  <!ENTITY sube "&#8838;">  <!ENTITY supe "&#8839;">  <!ENTITY oplus "&#8853;">  <!ENTITY otimes "&#8855;">  <!ENTITY perp "&#8869;">  <!ENTITY sdot "&#8901;">  <!ENTITY lceil "&#8968;">  <!ENTITY rceil "&#8969;">  <!ENTITY lfloor "&#8970;">  <!ENTITY rfloor "&#8971;">  <!ENTITY lang "&#9001;">  <!ENTITY rang "&#9002;">  <!ENTITY loz "&#9674;">  <!ENTITY spades "&#9824;">  <!ENTITY clubs "&#9827;">  <!ENTITY hearts "&#9829;">  <!ENTITY diams "&#9830;">'
    doctype = '<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd" [ {} ]>'.format(entities)
    xml = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>'
    doc = xml + doctype + svg
    # add namespaces
    doc = doc.replace("<svg ", '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" ')
    # use ElementTree for further modifications
    root = ET.fromstring(doc)
    # Find workspace group, remove other top elements
    workspace = root.find("svg:g", namespaces)
    path = root.find("svg:path", namespaces)
    defs = root.find("svg:defs", namespaces)
    root.remove(path)
    root.remove(defs)
    # Insert the CSS used in Scratch 
    root.insert(0, ET.fromstring('''<style xmlns="http://www.w3.org/2000/svg">
    .blocklyPath {
        stroke-width: 1px;
    }
    svg {
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    }
    .blocklyText {
        fill: #fff;
        font-family: "Helvetica Neue", Helvetica, sans-serif;
        font-size: 12pt;
        font-weight: 500;
    }
    .blocklyNonEditableText > text, .blocklyEditableText > text {
        fill: #575E75;
    }
    .blocklyNonEditableText > text.blocklyDropdownText, .blocklyEditableText > text.blocklyDropdownText {
        fill: #fff;
    }
    </style>
    '''))
    # Set some smallish dimensions (will be fixed outside this script later)
    root.attrib["width"] = "400"
    root.attrib["height"] = "80"
    # Remove second child element of workspace (blocks are in first)
    del workspace[1]
    # Unset clip path
    if "clip-path" in workspace.attrib:
        del workspace.attrib["clip-path"]
    # Move all blocks one level up under workspace
    canvas = workspace[0]
    for c in canvas:
        workspace.append(c)
    workspace.remove(canvas)
    # Remove all elements that are no blocks and
    # repair opcodes
    opcodes  = []
    for c in workspace:
        # Remove all transforms (they set the position of the blocks)
        if "transform" in c.attrib:
            del c.attrib["transform"]
        # All blocks have a data-id with (almost) an opcode
        if "data-id" in c.attrib:
            # Fix sensing_of
            if c.attrib["data-id"] == "of":
                c.attrib["data-id"] = "sensing_of"
            if "data-category" in c.attrib:
                # we use the data category to fix some opcodes
                # unfortunately, sounds and operators need to be renamed
                if c.attrib["data-category"] == "sounds":
                    c.attrib["data-category"] = "sound"
                if c.attrib["data-category"] == "operators":
                    c.attrib["data-category"] = "operator"
                if c.attrib["data-category"] == "events":
                    c.attrib["data-category"] = "event"
                # And for extensions they use translations... aaargh!
                if c.attrib["data-id"].startswith("pen"):
                    c.attrib["data-category"] = "pen"
                # some blocks have random id parts, we need to remove these
                parts = c.attrib["data-id"].split("_")
                for p in parts[::-1]:
                    if not_letters.search(p):
                        parts.remove(p)
                if len(parts)==0:
                    continue
                c.attrib["data-id"] = "_".join(parts) 
                # Finally, we can repair all blocks so that the id is the opcode
                if c.attrib["data-id"].startswith("|"):
                    c.attrib["data-id"] = c.attrib["data-id"][c.attrib["data-id"].index("_") + 1:]
                if not c.attrib["data-id"].startswith(c.attrib["data-category"]): 
                    c.attrib["data-id"] = c.attrib["data-category"] + "_" + c.attrib["data-id"]
            opcodes.append(c.attrib["data-id"])
    opcodes.sort()
    print(f"Found {len(opcodes)} blocks.")
    return opcodes, root
```

```python
def save_blocks(opcodes, root, language):
    Path(f"svg/{language}").mkdir(parents=True, exist_ok=True)
    for opcode in opcodes:
        # print(opcode)
        # Create a copy for this block
        root2 = copy.deepcopy(root)
        # remove everything else
        for c in root2[1][::-1]:
            if not "data-id" in c.attrib or c.attrib["data-id"]!=opcode:
                root2[1].remove(c)
        # Include the icon svg as nested svg (otherwise it gets blurred in inkscape)
        for imageparent in root2.findall('.//svg:image/..', namespaces):
            image = imageparent.find('svg:image', namespaces)
            index = list(imageparent).index(image)
            filename = image.attrib["{http://www.w3.org/1999/xlink}href"]
            # Extensions use data URIs...
            innersvg = ""
            if filename.startswith("data:image/svg+xml;base64,"):
                innersvg = filename[len("data:image/svg+xml;base64"):]
                innersvg = base64.decodebytes(innersvg.encode("utf-8")).decode("utf-8")
            else:
                with open(filename, "r", encoding="utf-8") as f:
                    innersvg = f.read()
            innersvg = innersvg[innersvg.index("<svg"):]
            newimage = ET.fromstring(f'''<g xmlns="http://www.w3.org/2000/svg">
                {innersvg}
            </g>
            ''')
            newimage[0].attrib["width"] = image.attrib["width"]
            newimage[0].attrib["height"] = image.attrib["height"]
            if "transform" in image.attrib:
                newimage.attrib["transform"] = image.attrib["transform"]
            imageparent.insert(index, newimage) 
            imageparent.remove(image)

        # display(SVG(ET.tostring(root2)))
        # Finally, write the SVG
        with open(f"svg/{language}/{opcode}.svg", "wb") as f:
            f.write(ET.tostring(root2))
```

```python
driver = start_selenium()
activate_extension(driver, "pen")
with open("langs.json", "r", encoding="utf-8") as f:
    languages = json.load(f)
    for lang in languages:
        print(f"Language {lang}")
        svg = scrape_blocks(driver, lang)
        opcodes, root = fix_svg_and_get_opcodes(svg)
        save_blocks(opcodes, root, lang)
```

```python

```

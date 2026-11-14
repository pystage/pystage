# Scratch fonts

The text fonts that Scratch 3 uses for text in costumes (the font menu of the
paint editor). They are taken unmodified from
[scratch-render-fonts](https://github.com/scratchfoundation/scratch-render-fonts)
(`src/`, commit `50c4f30a6d9478e5e094e2929afeba1a52dbd8fc`, package version 1.0.259),
the package Scratch itself uses to render SVG costumes. Every font is licensed
under the SIL Open Font License 1.1 (full text in `licenses/`). The fonts are
only used by pyStage to draw text; they are not modified, renamed or sold
separately.

| File | Font (name in the file) | Family in Scratch | Version | Copyright notice embedded in the font | Licence file | Upstream | SHA-256 |
|------|-------------------------|-------------------|---------|---------------------------------------|--------------|----------|---------|
| `NotoSans-Medium.ttf` (452608 bytes) | Noto Sans Medium | Sans Serif | 2.000 (noto-source 20170915) | Copyright 2015 Google Inc. All Rights Reserved. | `licenses/OFL-NotoSans.txt` (Noto Project Authors, https://github.com/googlefonts/noto-fonts) | https://github.com/googlefonts/noto-fonts | `c801b8d2522fb554678f17f4597158b1af3f9be3abd6ce35d5a3112a81e2bf39` |
| `SourceSerifPro-Regular.otf` (222380 bytes) | Source Serif Pro Regular | Serif | 2.000 | Copyright 2014, 2015, 2016 Adobe Systems Incorporated (http://www.adobe.com/), with Reserved Font Name 'Source'. | `licenses/OFL-SourceSerifPro.txt` (from tag 2.000R) | https://github.com/adobe-fonts/source-serif (identical to `OTF/SourceSerifPro-Regular.otf` of tag 2.000R) | `22892edbfe310d39952b37c7ef1f1b9a1053a01b5ee528b81296eec23cb94c7d` |
| `Handlee-Regular.ttf` (39132 bytes) | Handlee Regular | Handwriting | 1.001 | Copyright (c) 2011, Admix Designs (http://www.admixdesigns.com/) with Reserved Font Name Handlee. | `licenses/OFL-Handlee.txt` (from google/fonts `ofl/handlee`) | https://github.com/google/fonts/tree/main/ofl/handlee (identical file) | `7b99c0f291b5d52e06c66498a1d0dd6dff45a32e32d13be089c60d2d8dc00445` |
| `Knewave.ttf` (44664 bytes) | Knewave | Marker | 2.000 | Copyright (c) 2011 by Tyler Finck. All rights reserved. (licence field: OFL) | `licenses/OFL-Knewave.txt` (from google/fonts `ofl/knewave`) | https://github.com/google/fonts/tree/main/ofl/knewave (Google now ships a newer build; this is the file Scratch ships) | `c946330c5735b693abc6ef280d9cfdb1f95d503a8ee55a21db0965cedcb2eaf9` |
| `Griffy-Regular.ttf` (208776 bytes) | Griffy Regular | Curly | 1.000 | Copyright (c) 2012 by Font Diner, Inc DBA Neapolitan (diner@fontdiner.com) with Reseved Font Name "Griffy" | `licenses/OFL-Griffy.txt` (from google/fonts `ofl/griffy`) | https://github.com/google/fonts/tree/main/ofl/griffy (identical file) | `c889c3f8d169631386a297eae8b5bdefbf8d06aa9f4f325faec31b9b5f38eeb5` |

Scratch only offers the regular weight of each font (for Sans Serif its Medium
cut, which Scratch uses as the regular one); there is no bold or italic.

## Not bundled

* Pixel: Scratch uses Grand9K Pixel (Grand Chaos Productions), which is
  licensed under CC BY-SA 3.0 (ShareAlike), not under the OFL.
* Scratch (the title font, `Scratch.ttf`, "ScratchFont" by Jakob Fischer): only
  "Distribute freely" in the file, no real licence, the upstream site is gone.
* Chinese, Japanese, Korean: Scratch uses system fonts, so does pyStage.

For these, pyStage falls back to similar system fonts or to Roboto.

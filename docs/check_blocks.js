// Checks that scratchblocks recognises the "Scratch block:" lines of the docstrings.
// Reads the JSON written by check_blocks.py (path as argument or stdin) and prints every block
// that scratchblocks does not parse cleanly (unknown blocks get the category "obsolete").
//
// Needs the scratchblocks npm package (the vendored browser build needs a DOM):
//   mkdir -p /tmp/sb && cd /tmp/sb && npm pack scratchblocks@3.7.1 && tar xzf scratchblocks-3.7.1.tgz
//   SCRATCHBLOCKS_DIR=/tmp/sb/package node check_blocks.js blocks.json
// or run `npm install scratchblocks@3.7.1` outside the repository's tracked files (node_modules is ignored).
// Usually you run check_blocks.py, which does all of this.

import fs from "fs"
import path from "path"
import { pathToFileURL } from "url"

const dir = process.env.SCRATCHBLOCKS_DIR
const entry = dir
  ? pathToFileURL(path.join(dir, "syntax", "index.js")).href
  : "scratchblocks/syntax/index.js"
const { parse, loadLanguages } = await import(entry)

const localesDir = dir ? path.join(dir, "locales") : path.join("node_modules", "scratchblocks", "locales")
loadLanguages({ de: JSON.parse(fs.readFileSync(path.join(localesDir, "de.json"), "utf8")) })

const entries = JSON.parse(fs.readFileSync(process.argv[2] || 0, "utf8"))

// all problems of a block, including nested blocks in its inputs and bodies
function problems(block, found = []) {
  if (!block || typeof block !== "object") return found
  if (block.info && block.info.category === "obsolete") found.push(block.info.id || block.children?.map(c => c.value ?? "").join(" "))
  for (const child of block.children || []) problems(child, found)
  if (block.value && typeof block.value === "object") problems(block.value, found)
  if (block.blocks) for (const b of block.blocks) problems(b, found)
  return found
}

let bad = 0
for (const e of entries) {
  const doc = parse(e.text, { languages: [e.lang] })
  const blocks = doc.scripts.flatMap(s => s.blocks)
  const reasons = blocks.flatMap(b => problems(b))
  if (blocks.length === 0 || reasons.length) {
    bad++
    console.log(`${e.file}:${e.line} ${e.name}  [${e.lang}]  ${e.text}`)
  }
}
console.log(`${entries.length} blocks checked, ${bad} not recognised`)
process.exit(bad ? 1 : 0)

#!/bin/bash
# Crop all SVGs to their actual size
for i in $(find svg -name \*.svg)
do
	echo $i
	inkscape --export-area-drawing $i -o $i > /dev/null 2>&1
done

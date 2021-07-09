#!/bin/bash
# Export pngs
# Density can be used for scaling, 96 DPI is default
if [ -z "$1" ]
then
	density=96
else
	density=$1
fi


for i in $(find svg -name \*.svg)
do
	out=${i#svg}
	out="png${density}${out%svg}png"
	mkdir -p $(dirname "$out")
	echo "$i -> $out"
	inkscape $i -o $out -d $density > /dev/null 2>&1
done

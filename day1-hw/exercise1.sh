#!/bin/bash

#USAGE: bash exercise1.sh input_VCF

for nuc in C 
do
  echo "Considering " $nuc
  awk -v awkvar="$nuc" '/^#/{next} {if ($4 == awkvar) {print $5}}' $1 | sort | uniq -c
done

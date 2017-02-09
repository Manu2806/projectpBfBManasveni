#!/bin/bash

echo "Enter proteincode and press [ENTER]:"
#to obtain user input

read proteincode

$proteincode= proteincode
#to assign a variable to user input

curl --remote-name https://files.rcsb.org/view/$proteincode.pdb
#curl function with remote name for doenloading any pdb code file (defined by variable) from the website

grep ATOM $proteincode.pdb | grep -v REMARK | cut -c 18-21,24-26 | sort | uniq | cut -f 1 -d " " | uniq -c | sort -nr
#to display amino acid occurance in the protein on the interface



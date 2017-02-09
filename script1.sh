#!/bin/bash

echo "Enter (userinput) and press [ENTER]:"
#to obtain user input

read userinput

$userinput= userinput
#to assign a variable to user input

curl --remote-name https://files.rcsb.org/view/$userinput.pdb
#curl function with remote name for doenloading any pdb code file (defined by variable) from the website

grep ATOM $userinput.pdb | grep -v REMARK | cut -c (element position) | sort | uniq | cut -f 1 -d " " | uniq -c | sort -nr
#to display amino acid occurance in the protein on the interface



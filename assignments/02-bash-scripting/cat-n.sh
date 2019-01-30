#!/bin/bash
i=0
file=$1
if [[ $# -eq 0 ]]; then
        echo "Usage: cat-n.sh FILE"
        exit 1
fi
if [[ -f "$1" ]]; then
	while read -r line; do
                	i=$((i+1))
                	echo $i "$line";
        	done < "$file"
        exit
else     
        echo "$1 is not a file"
        exit 1
fi     

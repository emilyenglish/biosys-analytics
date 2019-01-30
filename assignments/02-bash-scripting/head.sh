#!/bin/bash
linezz=$2
linezz=${2:-3}
j=0
file=$1

if [[ $# -eq 0 ]]; then
        echo "Usage: head.sh FILE [NUMBER OF LINES]"
        exit 1
fi
if [[ ! -f "$1" ]]; then
	echo "$1 is not a file"
        exit 1
fi
if [[ $# -eq 1 ]]; then
	while read -r linezz; do
        	echo "$linezz"
        	j=$((j+1))
        	if [[ $j -eq 3 ]]; then
                	break
       		fi
done < "$file"
fi
if [[ $# -eq 2 ]]; then
	while read -r linezz; do
		echo "$linezz"
		j=$((j+1))
		if [[ $j -eq $2 ]]; then
			break
		fi
	done < "$file"
fi

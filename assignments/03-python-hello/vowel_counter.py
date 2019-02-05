#!/usr/bin/env python3
"""
Author : emilyenglish
Date   : 2019-02-04
Purpose: I count vowels
"""

import os
import sys


# --------------------------------------------------
def main():
    args = sys.argv[1:]
    num_vowels = 0
    vowels = set("AEIOUaeiou")
    if len(args) != 1:
        print('Usage: vowel_counter.py STRING'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)
    if len(args) == 1:
        string = args[0]
        for letter in string:
            if letter in vowels:
                num_vowels += 1
                
    if num_vowels == 1:
        print("There is 1 vowel in " + '"' + string + '."')
    if num_vowels > 1:
        print("There are", num_vowels, "vowels in " + '"' + string + '."')
    if num_vowels == 0:
        print("There are", num_vowels, "vowels in " + '"' + string + '."')
# --------------------------------------------------
main()

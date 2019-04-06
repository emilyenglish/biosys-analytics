#!/usr/bin/env python3
"""
Author : emilyenglish
Date   : 2019-04-05
Purpose: regex with passwords
"""

import os
import sys
import re


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 2:
        print('Usage: {} PASSWORD ALT'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)
     
    password = args[0]
    alt = args[1]
    length = len(alt) - 1
    alt_1 = str(alt)
    alt_2 = alt_1[:length]
    alt_3 = alt_2[1:]
    alt_4 = alt_1[1:]
   
    if str(password) == str(alt):
        print("ok")
    elif password.upper() == str(alt):
        print("ok")
    elif password.capitalize() == str(alt):
        print("ok")
    elif str(password) == str(alt_3) or str(password) == str(alt_2) or str(password) == str(alt_4):
        print("ok") 
    else:
        print("nah")

   


# --------------------------------------------------
main()

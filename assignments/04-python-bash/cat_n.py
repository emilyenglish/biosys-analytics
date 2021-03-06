#!/usr/bin/env python3
"""
Author : emilyenglish
Date   : 2019-02-05
Purpose: cat-n files
"""

import os
import sys


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} FILE'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)
    
    arg = args[0]
    if not os.path.isfile(arg):
        print('{} is not a file'.format(arg))
        sys.exit(1)
    if os.path.isfile(arg):
        with open(arg, 'r') as f:
            for i, line in enumerate(f):
                print(' {}: {}'.format(i+1, line.strip()))

# --------------------------------------------------
main()

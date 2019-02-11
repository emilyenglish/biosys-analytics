#!/usr/bin/env python3
"""
Author : emilyenglish
Date   : 2019-02-05
Purpose: head function
"""

import os
import sys


# --------------------------------------------------
def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print('Usage: {} FILE [NUM_LINES]'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)
    arg = args[0]
    j = 0
    if not os.path.isfile(arg):
        print('{} is not a file'.format(arg))
        sys.exit(1)
    if os.path.isfile(arg):
        if len(args) == 1:
            num_lines = 3
        if len(args) == 2:
            num_lines = int(args[1])
        if num_lines <= 0:
            print('lines ({}) must be a positive number'.format(num_lines))
            sys.exit(1)
        if num_lines > 0:
            with open(arg) as f:
                for j, line in enumerate(f, 1):
                    print(line, end="")
                    if j == num_lines:
                        break             
           

# --------------------------------------------------
main()

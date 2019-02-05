#!/usr/bin/env python3
"""
Author : emilyenglish
Date   : 2019-02-02
Purpose: Say Hello
"""

import os
import sys


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) == 0:
        print('Usage: {} NAME [NAME ...]'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)
    if len(args) == 1:
        print('Hello to the 1 of you:', args[0] + '!')
    elif len(args) == 2:
        print('Hello to the 2 of you:', args[0] + ' and ' + args[1] + '!')
    elif len(args) > 2:
        print("Hello to the", len(args), "of you:", ", ".join(args[:-1]) + ', and', args[-1] + '!')
        



# --------------------------------------------------
main()

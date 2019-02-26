#!/usr/bin/env python3
"""
Author : emilyenglish
Date   : 2019-02-21
Purpose: Prints out first line of contents of a file
"""

import argparse
import sys
import os
# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Print first lines of a file',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='DIR', help='directory', nargs ='+')
       

    parser.add_argument(
        '-w',
        '--width',
        help='int value for width of space to print',
        metavar='int',
        type=int,
        default=50)

    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)

# -------------------------------------------------

def readFile(entry):
    args = get_args()
    width = args.width
    with open(entry) as f:
        for line in f:
            print(line[:width])
            break
# --------------------------------------------------
def main():
    
    args = get_args()
    positional = args.positional
    width = args.width
    #print(args)
    #print('width  = "{}"'.format(width))
    #print('positional = "{}"'.format(positional))
   
    for arg in positional: 
        if not os.path.isdir(*positional):
            warn('"{}" is not a directory'.format(*positional))
        if os.path.isdir(*positional):
            print(*positional)
            for entry in sorted(os.listdir(*positional)):
                entry2 = os.path.join(*positional, entry)
                with open(entry2) as f:
                    for line in f:
                        i = 0
                        width2 = width - len(line)
                        print(line, end='') 
                        for i in range(0, width2): print('.', end='')
                        print(' '+ entry)
                        break 
         
 

# --------------------------------------------------
if __name__ == '__main__':
    main()


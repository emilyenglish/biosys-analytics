#!/usr/bin/env python3
"""
Author : emilyenglish
Date   : 2019-03-16
Purpose: Bottles of Beer song
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-n',
        '--num_bottles',
        help='Number of bottles',
        metavar='INT',
        type=int,
        default=10)

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


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    num_bottles  = args.num_bottles
    count = num_bottles
    
    
    if num_bottles < 1:
        die('N "{}" must be a positive number'.format(num_bottles))
    if num_bottles > 1: 
        while count != 2:
            print('{} bottles of beer on the wall,'.format(count))
            print('{} bottles of beer,'.format(count))
            count = count - 1
            print('Take one down, pass it around,')
            print("{} bottles of beer on the wall!\n".format(count))

        print("2 bottles of beer on the wall,")
        print("2 bottles of beer,")
        print("Take one down, pass it around,")
        print("1 bottle of beer on the wall!\n")
        print("1 bottle of beer on the wall,")
        print("1 bottle of beer,")
        print("Take one down, pass it around,")
        print("0 bottles of beer on the wall!")
    if num_bottles == 1:
        print("1 bottle of beer on the wall,")
        print("1 bottle of beer,")
        print("Take one down, pass it around,")
        print("0 bottles of beer on the wall!")
   
  

# --------------------------------------------------
if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Author : emilyenglish
Date   : 2019-04-09
Purpose: calc hamming distance
"""

import argparse
import sys
import logging
import os

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Hamming distance',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'FILE', metavar='FILE', help='File inputs', nargs = 2)

    parser.add_argument(
        '-d', '--debug', help='Debug', action='store_true')

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
def dist(s1, s2):
    """count = 0
    with open(s1, 'r') as f1:
        with open(s2, 'r') as f2:
            words1 = set(line.strip() for line in f1)
            words2 = set(line.strip() for line in f2)
    print(words1)
    print(words2)"""
    diff = 0   
    #bytesS1=bytes(s1)
    #bytesS2=bytes(s2, encoding="ascii")
    if os.path.isfile(s1):
        f1 = open(s1, 'r')
        words1 = list(f1.read().split())
    
        f2 = open(s2, 'r')
        words2 = list(f2.read().split())
    else:
        words1 = s1 
        words2 = s2
    i=0
    a = list(zip(words1, words2))
    for i in range(len(a)):
        
        if len(a[i][0]) > len(a[i][1]):
            j=0
            for j in range(len(a[i][0])):
                l = len(a[i][0])
                b= a[i][1].ljust(l,'0')
                #print(b)
                #print(a[i][0][j], b[i][1][j])
                if a[i][0][j] != b[i][1][j]:
                    diff += 1
                    j += 1
                    
        elif len(a[i][0]) < len(a[i][1]):
            k=0
            for k in range(len(a[i][1])):
                l = len(a[i][1])
                b = a[i][0].ljust(l,'0')
                #print(b)
                #print(b[k], a[i][1][k])               
                if b[k] != a[i][1][k]:
                    diff += 1
                    k += 1
                    
        else:
            h=0
            for h in range(len(a[i][1])):
                #print(a[i][0][h], a[i][1][h])
                if a[i][0][h] != a[i][1][h]:
                    diff += 1
                    h += 1
        i += 1 
                    
    print(diff)
    #print(a[i][0], a[i][1])
            
    #open two files at same time, read word by word, read into an array, zip words to pair, pass to function that tells the distance
    #use sum sum([1,2,...]), map sum(map(dist, words))
    
# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    File1 = args.FILE[0]
    File2 = args.FILE[1]
    unbug = args.debug
    #print(File1, File2)
    if not os.path.isfile(File1):
        die('"{}" is not a file.'.format(File1))
    if not os.path.isfile(File2):
        die('"{}" is not a file'.format(File2))
    logging.basicConfig(
        filename='.log',
        filemode='w',
        level=logging.DEBUG if args.debug else logging.CRITICAL
        )  
    dist(File1, File2)
    
    #dict(zip(a, l))    



# --------------------------------------------------
if __name__ == '__main__':
    main()

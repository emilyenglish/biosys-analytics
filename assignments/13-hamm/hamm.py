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
def dist6(seq1, seq2):
    print("hi")
    
# --------------------------------------------------
def dist(seq1, seq2):
    count = sum(1 for a, b in zip(seq1, seq2) if a != b) + abs(len(seq1) - len(seq2))
    return(count)
# --------------------------------------------------
def dist3(s1, s2):
    k = 0
    i =0
    diff = 0
    for k in range(len(s1[i])):
        if s2[k] != s1[k]:
            diff += 1
            k += 1
    print(diff)
# --------------------------------------------------
def dist2(s1, s2):
    diff = 0   
    i=0
      
    f1 = open(s1, 'r')
    words1 = list(f1.read().split())
    
    f2 = open(s2, 'r')
    words2 = list(f2.read().split())
   
         
    a = list(zip(words1, words2))
    for i in range(len(a)):
        
        if len(a[i][0]) > len(a[i][1]):
            j=0
            for j in range(len(a[i][0])):
                l = len(a[i][0])
                b= a[i][1].ljust(l,'0')
                diff = dist(a[i][0], b[i])
                count = count + diff
                #print(b)
                #print(a[i][0][j], b[i][1][j])
                """if a[i][0][j] != b[i][1][j]:
                    diff +=
                    j += 1"""
                    
        elif len(a[i][0]) < len(a[i][1]):
            k=0
            for k in range(len(a[i][1])):
                l = len(a[i][1])
                b = a[i][0].ljust(l,'0')
                diff = dist(b[i], a[i][1])
                count = count + diff
                #print(b)
                #print(b[k], a[i][1][k])               
                """if b[k] != a[i][1][k]:
                    diff += 1
                    k += 1"""
                    
        else:
            h=0
            for h in range(len(a[i][1])):
                diff = dist(a[i][0], a[i][1])
                count = count + diff
                #print(a[i][0][h], a[i][1][h])
                """if a[i][0][h] != a[i][1][h]:
                    diff += 1
                    h += 1"""
        i += 1 
    print(count)
                    
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
    f1 = open(File1, 'r')
    words1 = list(f1.read().split())
    f2 = open(File2, 'r')
    words2 = list(f2.read().split())             
    a = list(zip(words1, words2))
    dist(File1, File2)
    diff = 0
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
    """count = 0
    for i in range(len(a)):
        if len(a[i][0]) > len(a[i][1]):
            j=0
            for j in range(len(a[i][0])):
                l = len(a[i][0])
                b= a[i][1].ljust(l,'0') 
                dist(a[i][0], b[k])
                count += 1 
        elif len(a[i][0]) < len(a[i][1]):
            k=0
            for k in range(len(a[i][1])):
                l = len(a[i][1])
                b = a[i][0].ljust(l,'0')
                dist(b[k], a[i][1])
                count += 1
        else: 
            k=0
            for k in range(len(a[i][1])):
                l = len(a[i][1])
                b = a[i][0].ljust(l,'0')
                dist(b[k], a[i][1])
                count += 1
        print(count)"""           
    #dict(zip(a, l))    



# --------------------------------------------------
if __name__ == '__main__':
    main()

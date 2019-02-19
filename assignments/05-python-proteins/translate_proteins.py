#!/usr/bin/env python3
"""
Author : emilyenglish
Date   : 2019-02-14
Purpose: translate proteins
"""

import argparse
import sys
import os

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Translate DNA/RNA to proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='STR', help='DNA/RNA sequence')

    parser.add_argument(
        '-c',
        '--codons',
        help='A file with codon translations',
        metavar='FILE',
        type=str,
        default='None',
        required=True)

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output filename',
        metavar='FILE',
        type=str,
        default='out.txt')

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
    
    args = get_args()
    codons = args.codons
    outfile = args.outfile
    positional = args.positional    
    
    #print('STR = "{}"'.format(positional))
    #print('codons = "{}"'.format(codons))
    #print('outfile = "{}"'.format(outfile))
    if not os.path.isfile(codons):
        die('--codons "{}" is not a file'.format(codons))    

    codondict = {}
    with open(codons) as f:
        for line in f:
            (key, val) = line.split()
            codondict[str(key)] = val
    #print(codondict)  

    if codons != None and positional != None and outfile == None:
        outfile = 'out.txt'     
        out_fh = open(outfile, 'wt')
        k=3
        i=0
        n=len(positional)-k+1
        for i in range(0, n, k):
            c = positional[i:i+k]
            c = c.upper()
            if c in codondict:
                out_fh.write(codondict[c])
            else:
                out_fh.write('-')
        out_fh.close()
        print('Output written to "{}"'.format(outfile))
    if codons != None and positional != None and outfile != None:
        out_fh = open(outfile, 'wt')
        k=3
        i=0
        n=len(positional)-k+1
        for i in range(0, n, k):
            c = positional[i:i+k]
            c = c.upper()
            if c in codondict:
                out_fh.write(codondict[c])
            else:
                out_fh.write('-')
        out_fh.close()
        print('Output written to "{}"'.format(outfile))
# -------------------------------------------------
if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Author : emilyenglish
Date   : 2019-02-26
Purpose: fasta gc segregator
"""

import argparse
import sys
from collections import Counter
import os
from Bio import SeqIO
# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Segregate FASTA sequences by GC content',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'FASTA', metavar='FASTA', help='fasta file', nargs = '+')

    parser.add_argument(
        '-o',
        #SeqIO.write(record, out.fh, out_fmt)
        '--out_dir',
        help='A named string argument',
        metavar='DIR',
        type=dir,
        default='out')

    parser.add_argument(
        '-p',
        '--pct_gc',
        help='A named integer argument',
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


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    FASTA = args.FASTA
    out_dir = args.out_dir
    pct_gc = args.pct_gc
    
    files = 0
    totnum = 0
    for file in FASTA:
        if not os.path.isfile(file):
            print(('"{}" is not a file').format(file))
        else:
            num = 0
            files +=1
            basename = os.path.basename(file)
            highout_name = os.path.splittext(basename) [0] + '_' + 'high' +os.path.splittext(basename) [1]
            lowout_name = os.path.splittext(basename) [0] + '_' + 'low' + os.path.splittext(basename) [1]
            high = os.path.join(dirname, highout_name)
            low = os.path.join(dirname, highout_name)            
            high_fh = open(high, 'wt')
            low_fh = open(low, 'wt')
            #highout=os.path.splittext(name) 
            for record in SeqIO.parse(file, 'fasta'):
                num += 1
                seqlen= len(record.seq)
                dna = Counter((record.seq))
                gc = dna.get('G', 0) +dna.get('C', 0)
                print(record.seq)
                print(int(gc/seqlen*100))
                gc1= int(gc/seqlen*100)
                print('HIGH' if gc1 >= pct_gc else 'LOW')
            if gc1 >= pct_gc:
                SecIO.write(seq_record, high_fh, "fasta")
            else: 
                SecIO.write(seq_record, low_fh, "fasta")
            #splitext
            #09 - python parsing for help
# --------------------------------------------------
if __name__ == '__main__':
    main()

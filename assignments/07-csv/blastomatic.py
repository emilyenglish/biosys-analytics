#!/usr/bin/env python3
"""
Author : emilyenglish
Date   : 2019-03-09
Purpose: CSV Parsing
"""

import argparse
import sys
import os
from Bio import SeqIO
from Bio.Blast import NCBIXML
import csv
import pprint
import pandas

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Annotate BLAST output',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'FILE', metavar='FILE', help='BLAST output (-outfmt 6)')

    parser.add_argument(
        '-a',
        '--annotations',
        help='Annotation file',
        metavar='FILE',
        type=str,
        default='')

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output file',
        metavar='FILE',
        type=str,
        default='')

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
    FILE = args.FILE
    annotations = args.annotations
    outfile = args.outfile
   
   
    if not os.path.isfile(FILE):
        die('"{}" is not a file'.format(FILE))
    if not os.path.isfile(annotations):
        die('"{}" is not a file'.format(annotations))
    if os.path.isfile(FILE) and os.path.isfile(annotations):
        reader = csv.DictReader(open(FILE), delimiter = '\t', fieldnames = ("qseqid", "sseqid", "pident", "length", "mismatch", "gapopen", "qstart", "qend", "sstart", "send", "evalue", "bitscore"))
        reader_a = csv.DictReader(open(annotations), fieldnames = ("centroid", "domain", "kingdom", "phylum", "class", "order", "genus", "species"))
        reader_b = csv.reader(open(annotations, 'r'))
        anno_dict = {}
        for row in reader_b:
            key1 = row[0]
            anno_dict[key1] = row[1:]

        #print(anno_dict)
       
        """for dct in map(dict, reader_a):
            genus = (f"{dct['genus']}")
            species = (f"{dct['species']}")
            if genus == "":    
                print("NA")
            else:
                print(genus)
            if species == "":
                print("NA")
            else:
                print(species)"""
        for dct in map(dict, reader):
            seq_id = (f"{dct['sseqid']}")           
            pident = (f"{dct['pident']}")
            #print(seq_id)
            for dct_a in map(dict, reader_a):
                genus = (f"{dct_a['genus']}")
                species = (f"{dct_a['species']}")
            if any(seq_id == key for key in anno_dict):    
                """print(seq_id)
                print(pident)
                print(genus)
                print(species)
                #find a way to print genus and species of seq_id
                """
                
            else:
                warn('Cannot find seq "{}" in lookup'.format(seq_id))
        """for line_a in reader_a:
            an_id = (line_a['centroid']) 
            print('"{}" is an_id'.format(an_id))             
        for line in reader:
            seq_id = (line['sseqid'])
            print('"{}" is seq_id'.format(seq_id))
        if seq_id == an_id:
            print("hi")
        else:
            warn('Cannot find seq "{}" in lookup'.format(seq_id))
           """
        #pprint.pprint(dict_list)
        #pprint.pprint(dict_list_a)
        #for key, value in d1.items():
            #if key is 'sseqid':
                #print(value)
        #print(dict_list_a['centroid'])     

# --------------------------------------------------
if __name__ == '__main__':
    main()

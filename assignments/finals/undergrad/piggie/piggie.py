#!/usr/bin/env python3
"""
Author : emilyenglish
Date   : 2019-05-06
Purpose: pig latin from a file
"""

import argparse
import sys
import os
import re
import string

# --------------------------------------------------
def get_args():
    
    parser = argparse.ArgumentParser(
        description='Convert lines in a file to pig latin',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'STR', metavar='STR', help='String or File you want to convert')

    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
   
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    
    warn(msg)
    sys.exit(1)

# --------------------------------------------------
def validate_file(fileName):
    try:
        inputFile= open(fileName, 'r')
        inputFile.close()
    except IOError:
        print('File not found.')
# --------------------------------------------------
def strip_punctuation(line):
    punctuation = ''
    line = line.strip()
    #re.sub("[^a-zA-Z0-9']", '', line)
    #if len(line)>0:
        #if line[-1] in ('.','!','?',','):
            #punctuation = line[-1]
            #line = line[:-1]
    return line , punctuation
# --------------------------------------------------

def convert_file(fileName):
    inputFile= open(fileName, 'r')
    converted_lines = []
    for line in inputFile:
        #line, punctuation = strip_punctuation(line)
        line = line.split()
        new_words = []
        for word in line:
            wordb = re.sub("[^a-zA-Z0-9']", '', word)
            #print(wordb)
            consonants = re.sub("[aeiouAEIOU]", '', string.ascii_letters)
            match = re.match('^([' + consonants + ']+)(.+)', wordb)
            if match:
                #endString= str(word[1:])
                #them=endString, str(word[0:1]), 'ay'
                them = '-'.join([match.group(2), match.group(1) + 'ay'])
            else:
                them = wordb + '-yay'
            new_word="".join(them)
            new_words.append(new_word)
        new_sentence = ' '.join(new_words)
        #new_sentence = new_sentence.lower()
        #if len(new_sentence):
        #    new_sentence = new_sentence[0] + new_sentence[1:]
        converted_lines.append(new_sentence + ' ')
    return converted_lines
# -------------------------------------------------

def main():
    args = get_args()
    fileName= args.STR
    #if len(args) != 1:
        #die(usage: piggie.py [-h] STR)
    
    if not os.path.isfile(fileName):
        words = fileName
        wordList = re.sub("[^\w]", " ",  words).split()
        new_words = []
        for word in wordList:
            wordb = re.sub("[^a-zA-Z0-9']", '', word)
            consonants = re.sub('[aeiouAEIOU]', '', string.ascii_letters)
            match = re.match('^([' + consonants + ']+)(.+)', wordb)
            if match:
                them = ('-'.join([match.group(2), match.group(1) + 'ay']))
            else:
                them = (wordb + '-yay')
            new_word="".join(them)
            new_words.append(new_word)
        new_sentence = ' '.join(new_words)  
            
        print(new_sentence)
    #validate_file(fileName)
    else:
        new_lines = convert_file(fileName)
        for line in new_lines:
            print(line)
if __name__ == '__main__':
    main()

# --------------------------------------------------

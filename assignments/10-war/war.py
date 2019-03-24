#!/usr/bin/env python3
"""
Author : emilyenglish
Date   : 2019-03-19
Purpose: simplified war card game
"""

import argparse
import sys
import itertools
import random
# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Let us play the game of war',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    
    parser.add_argument(
        '-s',
        '--seed',
        help='Random seed',
        metavar='int',
        type=int,
        default=None)

    

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
    SEED = args.seed
    
    deck = [('♥2',2),('♥3',3),('♥4',4),('♥5',5),('♥6',6),('♥7',7),('♥8',8),('♥9',9),('♥10',10),('♥J',11),('♥Q',12),('♥K',13),('♥A',14),('♠2',2),('♠3',3),('♠4',4),('♠5',5),('♠6',6),('♠7',7),('♠8',8),('♠9',9),('♠10',10),('♠J',11),('♠Q',12),('♠K',13),('♠A',14),('♣2',2),('♣3',3),('♣4',4),('♣5',5),('♣6',6),('♣7',7),('♣8',8),('♣9',9),('♣10',10),('♣J',11),('♣Q',12),('♣K',13),('♣A',14),('♦2',2),('♦3',3),('♦4',4),('♦5',5),('♦6',6),('♦7',7),('♦8',8),('♦9',9),('♦10',10),('♦J',11),('♦Q',12),('♦K',13),('♦A',14)] 
     
    deck.sort(key=lambda x: x[0])
    #print(deck)
    #print(" ")
    if not SEED == None:
        random.seed(SEED)
        random.shuffle(deck)
    #print(deck)
        deck.reverse()
    #print(deck)
    p1_score = 0
    p2_score = 0
    count = 26
    while count > 0:
        p1_play = deck.pop(0)
        p2_play = deck.pop(0)
        p1 = p1_play[1]
        p2 = p2_play[1]
        if p1 > p2:
            p1_score = p1_score + 1
            print(p1_play[0],p2_play[0]+ ' P1')
        if p2 > p1:
            p2_score = p2_score + 1
            print(p1_play[0],p2_play[0]+ ' P2')
        if p2 == p1:
            print(p1_play[0],p2_play[0]+ ' WAR!')
        count = count -1
    if p1_score > p2_score:
        print("P1 {} P2 {}: Player 1 wins".format(p1_score, p2_score))
    if p2_score > p1_score:
        print("P1 {} P2 {}: Player 2 wins".format(p1_score, p2_score))
    if p1_score == p2_score:
        print("P1 {} P2 {}: DRAW".format(p1_score, p2_score))
# --------------------------------------------------
if __name__ == '__main__':
    main()

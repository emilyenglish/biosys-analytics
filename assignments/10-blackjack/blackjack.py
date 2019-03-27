#!/usr/bin/env python3
"""
Author : emilyenglish
Date   : 2019-03-26
Purpose: simplified blackjack card game
"""

import argparse
import sys
import random


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Let us play blackjack',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-s',
        '--seed',
        help='Random seed',
        metavar='int',
        type=int,
        default=None)

    parser.add_argument(
        '-p', '--player_hits', help='A boolean flag', action='store_true')
    parser.add_argument(
        '-d', '--dealer_hits', help='A boolean flag', action='store_true')
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
    playerhits = args.player_hits
    dealerhits = args.dealer_hits

    deck = [('♥2',2),('♥3',3),('♥4',4),('♥5',5),('♥6',6),('♥7',7),('♥8',8),('♥9',9),('♥10',10),('♥J',10),('♥Q',10),('♥K',10),('♥A',1),
('♠2',2),('♠3',3),('♠4',4),('♠5',5),('♠6',6),('♠7',7),('♠8',8),('♠9',9),('♠10',10),('♠J',10),('♠Q',10),('♠K',10),('♠A',1),
('♣2',2),('♣3',3),('♣4',4),('♣5',5),('♣6',6),('♣7',7),('♣8',8),('♣9',9),('♣10',10),('♣J',10),('♣Q',10),('♣K',10),('♣A',1),
('♦2',2),('♦3',3),('♦4',4),('♦5',5),('♦6',6),('♦7',7),('♦8',8),('♦9',9),('♦10',10),('♦J',10),('♦Q',10),('♦K',10),('♦A',1)] 

    deck.sort(key=lambda x: x[0])
    #print(deck)
    #print(" ")
    random.seed(SEED)
    random.shuffle(deck)
    #print(deck)
    
    player_c1 = deck.pop()
    dealer_c1 = deck.pop()
    player_c2 = deck.pop()
    dealer_c2 = deck.pop()
    player_sum = player_c1[1] + player_c2[1]
    dealer_sum = dealer_c1[1] + dealer_c2[1]
    a = dealer_c1[0]
    b = player_c1[0]
    c = dealer_c2[0]
    d = player_c2[0]    

    if playerhits == 1 and dealerhits == 0:
        player_c3 = deck.pop()
        e = player_c3[0]
        player_sum = player_c1[1] + player_c2[1] + player_c3[1]
        print("D [{:>2}]: {:<2} {:<2}".format(dealer_sum, a, c))
        print("P [{:>2}]: {:<2} {:<2} {:<2}".format(player_sum, b, d, e))
    elif dealerhits == 1 and playerhits == 0:
        dealer_c3 = deck.pop()
        f = dealer_c3[0]
        dealer_sum = dealer_c1[1] + dealer_c2[1] + dealer_c3[1]
        print("D [{:>2}]: {:<2} {:<2} {:<2}".format(dealer_sum, a, c, f))
        print("P [{:>2}]: {:<2} {:<2}".format(player_sum, b, d))
    elif playerhits == 0 and dealerhits == 0:
        print("D [{:>2}]: {:<2} {:<2}".format(dealer_sum, a, c))
        print("P [{:>2}]: {:<2} {:<2}".format(player_sum, b, d))
    elif playerhits == 1 and dealerhits == 1: 
        player_c3 = deck.pop()
        dealer_c3 = deck.pop()
        f = dealer_c3[0]
        e = player_c3[0]
        player_sum = player_c1[1] + player_c2[1] + player_c3[1]
        dealer_sum = dealer_c1[1] + dealer_c2[1] + dealer_c3[1]
        print("D [{:>2}]: {:<2} {:<2} {:<2}".format(dealer_sum, a, c, f)) 
        print("P [{:>2}]: {:<2} {:<2} {:<2}".format(player_sum, b, d, e))
    
    if dealer_sum > 21:
        print("Dealer busts.")
        exit(0)
    if player_sum > 21:
        print("Player busts! You lose, loser!")
        exit(0)
    if dealer_sum > 21 and player_sum > 21:
        print("Dealer busts.\nPlayer busts! You lose, loser!")
        exit(0)
    if dealer_sum == 21:
        print("Dealer wins!")
        exit(0)
    if player_sum == 21:
        print("Player wins. You probably cheated.")
        exit(0)
    if dealer_sum < 18:
        print("Dealer should hit.")
    if player_sum < 18:
        print("Player should hit.") 
   
      
        
# --------------------------------------------------
if __name__ == '__main__':
    main()

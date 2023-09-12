#!/usr/bin/env python3

'''demonstration of the probablity of getting a head(or a tail) on randon coin toss.
   My objective is to consolidate my knowledge of monte carlo simulation.
'''

'''Objective of the exercise: To determine the probablity of getting heads/tails
   Mathematical Probablity of heads or tails = 0.50
'''
import random

def coin_toss(trials: int):
    success = 0
    for trial in range(trials):
        toss = random.choice(['head', 'tail'])
        if toss == 'head':
            success += 1
        print(f"The number of trials are {trial+1} and number of heads are {success} ")
    probablity_head = success / trials
    return  probablity_head

def main():
    result = coin_toss(10000)
    print(f"The final probablity of getting a Head is {result}")

if __name__ == "__main__":
    main()

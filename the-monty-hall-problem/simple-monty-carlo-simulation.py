#!/usr/bin/env python3

'''
Understanding Monte-carlo simulation.
Monte- Carlo simulation takes into consideration the probablity distribution on an occuring event and expands it across multiple trials.
The final probablity of the event is calculated after dividing the successful intended attempts by the number of trials.
'''

#example of monte carlo simulation
#determining the probablity of a unique number on the dice when the dice is thrown multiple times

'''mathematically this number can be derived by the following formula
unique number in multiple throws = 6/6 * 5/6 * 4/6 * 3/6 * 2/6 * 1/6
this can be written as 6!/6^6

'''
import random
import math

def unique_number_mcs(trials:int):
    '''takes the number of trials and the number of unique digits as a parameter and returns
        the probablity of the unique digits across different throws
    '''
    success = 0
    for trial in range(trials):
        result = set()
        for roll in range(6):
            roll = random.randint(1, 6)
            result.add(roll)
            if len(result) == 6:
                success += 1
        print(f"Trial Number: {trial+1} and the success count is {success}")
    final_probablity = success / trials
    return final_probablity

def mp_unqiue_number():
    return math.factorial(6)/math.pow(6,6)

def main():
    unique_number_probablity = unique_number_mcs(100000)
    print(f"Final probablity using Monte Carlo Simulaion is: {unique_number_probablity:.4f}")
    print(f"Mathematically calculated probablity is: {mp_unqiue_number():.4f}")

if __name__ == '__main__':
    main()

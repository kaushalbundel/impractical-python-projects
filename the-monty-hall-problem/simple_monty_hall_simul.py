#!/usr/bin/env python3

'''Monty Hall Problem Simulation
As host of the TV game show Let's Make a Dea, Monty hall would show contestents three closed doors and ask them to choose one.
Behind one door was a valuable prize, behind other two were smelly goats. As soon as the contestant chose a door, Monty would open
one of the remaining door to reveal a goat. The contestent was given a choice, to remain with the door or to switch the door.

Marilyn vos Savant prepositioned that the best option is to switch the door.

'''

'''Objective: The objective of the activity is to prove that von Savant was correct'''

import random

def monty_hall_solution(trials:int):
    doors = ['A', 'B', 'C']  # signifying the three doors A, B and C
    success = 0
    for trial in range(trials):
        winner = random.choice(doors)
        contestant_choice = random.choice(doors)
        if winner == contestant_choice:
            success += 1
        print(f"The number of trials are {trial} and the trials with same choice as winner are {success}")
    final_result = success/trials
    return final_result

def main():
    probablity = monty_hall_solution(10000)
    print(f"The final probablity of contestant choice as winning door is {probablity}")

if __name__ == "__main__":
    main()

# The probablity of the prize being the same as the winner is on an average 33% which means that the chances of flipping the choice is 66%

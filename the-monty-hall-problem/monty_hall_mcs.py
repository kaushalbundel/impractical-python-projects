#!/usr/bin/env python3
'''Program to determine Monty hall problem using Monty-Carlo simulation(as per the book)
Step 1. create a function to enter the number of prompts (trials) for the function
Step 2. create a the monte-carlo simulation
'''

import random

def user_prompt(prompt, default=None):
    '''Allow the use of default values in input'''
    prompt = f"{prompt} [{default}] : "
    response = input(prompt)
    if not prompt and response:
        return default
    else:
        return response


num_turns = user_prompt("Please enter the number of turns, the default is ",
                        "20000")

wins_correct_pick = 0
wins_switch = 0
doors = ['a', 'b', 'c']
num_turns = int(num_turns)

for turns in range(num_turns):
    chose_player = random.choice(doors)
    chose_game = random.choice(doors)
    if chose_player == chose_game:
        wins_correct_pick += 1
    else:
        wins_switch += 1

print(f"The number of games played {num_turns}")
print(f"The number of correct picks by the player are {wins_correct_pick}")
print(f"The number of wins by switching needed are {wins_switch}")
print(f"The probablity of winning bv the first pick of the player, {wins_correct_pick/num_turns:.2f}")
print(f"The probablity of winning bv the switching options is , {wins_switch/num_turns:.2f}")

input("Press Enter to exit the console")  # exiting the game

#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import random
import eddy as p2
import randint13
import roy
import rc   as p1
import darren
import johnson

"""
The Challenge
There are two players.
Each player writes a number, hidden from the other player. It can be any integer 1 or greater.
The players reveal their numbers.
Whoever chose the lower number gets 1 point, unless the lower number is lower by only 1,
then the player with the higher number gets 2 points.
If they both chose the same number, neither player gets a point.
This repeats, and the game ends when one player has 5 points.
The challenge is to write a script to play this game.
Knowing the rules and all your opponent’s previous numbers, can you program a strategy?
"""

"""
scores: current score of this game
player_one_nums: a list of guesses from opponent this iteration
player_two_nums: a list of guesses from you this iteration
total_iterations: how many games we are playing (100)
current_iteration: the current game #
player_one_nums_history: opponents and all previous game and their answers in order
outcomes: the current overall iteration score
"""
def player_one(scores, player_one_nums, player_two_nums, total_iterations, current_iteration,
                player_two_nums_history, outcomes):
    b = random.randrange(1,3)
    print b
    return b

def player_two(scores, player_one_nums, player_two_nums,
        total_iterations, current_iteration, player_one_nums_history, outcomes):
    #return random.randrange(1,4)
    a = p1.play_game(scores, player_one_nums, player_two_nums,
        total_iterations, current_iteration, player_one_nums_history, outcomes)
    print a
    return a

def compute_score(player_one_answer, player_two_answer, scores):
    if player_one_answer + 1 == player_two_answer:
        scores['Player_Two'] += 2
    elif player_two_answer + 1 == player_one_answer:
        scores['Player_One'] += 2
    elif player_one_answer < player_two_answer:
        scores['Player_One'] += 1
    elif player_one_answer > player_two_answer:
        scores['Player_Two'] += 1
    return scores

def calculate_winner(scores, outcomes):
    if scores['Player_One'] > scores['Player_Two']:
        outcomes['Player_One'] += 1
    elif scores['Player_Two'] > scores['Player_One']:
        outcomes['Player_Two'] += 1
    else:
    #this shouldn't be possible unless they aren't using an integer
        outcomes['ties'] += 1
    return outcomes

def main():
    total_iterations = 100
    scores = {'Player_One': 0, 'Player_Two': 0}
    outcomes = {'Player_One': 0, 'Player_Two': 0, 'ties': 0}
    player_one_nums = []
    player_one_nums_history = []
    player_two_nums = []
    player_two_nums_history = []
    valid = True
    for current_iteration in range(1, total_iterations+1):
        while scores['Player_One'] < 5 and scores['Player_Two'] < 5 and valid:
            scores1 = {'Player_One': scores['Player_Two'], 'Player_Two': scores['Player_One']}
            outcomes1 = {'Player_One': outcomes['Player_Two'], 'Player_Two': outcomes['Player_One'], 'ties': 0}
            player_one_answer = p1.play_game(
                scores1, player_two_nums,player_one_nums, total_iterations, current_iteration,
                player_two_nums_history, outcomes1)
            player_two_answer = p2.play_game(
                scores, player_one_nums, player_two_nums, total_iterations, current_iteration,
                player_one_nums_history, outcomes)
            if (isinstance(player_one_answer, int) and player_one_answer>0):
                player_one_nums.append(player_one_answer)
            else:
                print "Player one lose, did NOT receive a natural number"
                valid = False
                break
            if (isinstance(player_two_answer, int) and player_two_answer>0):
                player_two_nums.append(player_two_answer)
            else:
                print "Player two lose, did NOT receive a natural number"
                valid = False
                break
            compute_score(player_one_answer, player_two_answer, scores)
        calculate_winner(scores, outcomes)
        scores = {'Player_One': 0, 'Player_Two': 0}
        player_one_nums_history.append({'iteration':current_iteration,
            'opponent_guesses':player_one_nums})
        player_two_nums_history.append({'iteration':current_iteration,
            'opponent_guesses':player_two_nums})
        player_one_nums = []
        player_two_nums = []

    print('Results - Player One {0}, Player Two {1}, Tie {2}'.format(
        outcomes['Player_One'], outcomes['Player_Two'], outcomes['ties']))


if __name__ == '__main__':
    main()

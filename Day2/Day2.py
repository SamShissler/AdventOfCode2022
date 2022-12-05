# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 23:49:27 2022

@author: samsh

Advent of Code 2022 Day 2

Rock paper scissors

Part 1

Game outcome
Loss = 0 pts
Draw = 3 pts
Win = 6 pts

Plays
Rock = A,X = 1 pt
Paper = B,Y = 2 pts
Scissors = C,Z = 3 pts

Part 2

Game outcome
X = Loss
Y = Draw
Z = Win

"""

"""
    Part 1
"""
f = open("input.txt", "r")

total_score = 0

for line in f:
    opp, exp = line.split()
    round_score = 0
    if(exp == "X"):
        round_score+=1
    elif(exp == "Y"):
        round_score += 2
    elif(exp == "Z"):
        round_score += 3
    if(opp == "A"):
        if(exp == "X"):
            round_score += 3
        elif(exp == "Y"):
            round_score += 6
    elif(opp == "B"):
        if(exp == "Y"):
            round_score += 3
        elif(exp == "Z"):
            round_score += 6
    elif(opp == "C"):
        if(exp == "Z"):
            round_score += 3
        elif(exp == "X"):
            round_score += 6
    total_score += round_score
    #print(opp, exp, round_score)
print(total_score)
f.close()
"""
    Part 2
"""

f = open("input.txt", "r")

total_score = 0
a = 1
b = 2
c = 3

for line in f:
    opp, exp = line.split()
    round_score = 0
    if(exp == "Y"):
        round_score += 3
    elif(exp == "Z"):
        round_score += 6
    if(opp == "A"):
        if(exp == "Y"):
            round_score += a
        elif(exp == "Z"):
            round_score += b
        elif(exp == "X"):
            round_score += c
    elif(opp == "B"):
        if(exp == "Y"):
            round_score += b
        elif(exp == "Z"):
            round_score += c
        elif(exp == "X"):
            round_score += a
    elif(opp == "C"):
        if(exp == "Y"):
            round_score += c
        elif(exp == "Z"):
            round_score += a
        elif(exp == "X"):
            round_score += b
    total_score += round_score
    #print(opp, exp, round_score)
print(total_score)
f.close()
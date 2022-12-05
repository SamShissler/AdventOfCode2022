# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 00:40:12 2022

@author: samsh
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 00:40:12 2022

@author: samsh

Advent of Code 2022 Day 3

Rucksack Reorganization

"""


"""
    Part 1
"""

alph = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

f = open("input.txt", "r")

total_priority = 0
numLines= 0
numAnomlu = 0

def find_anomoly(sack):
    for i in range(int(len(sack)/2)):
        for j in range(int(len(sack)/2)):
            if(sack[i] == sack[len(sack)-j-1]):
                #anomoly found
                #print("Anomaly found: ", sack[i])
                return sack[i]



for sack in f:
    prio = 0
    sack = sack.strip()
    anom = find_anomoly(sack)
    if anom is not None:
        numAnomlu += 1
        prio += alph.find(anom)+1
    total_priority += prio
        
    #print(sack)
    numLines += 1
print(total_priority)
#print(numAnomlu)
#print(numLines)
f.close()

"""
    Part 1
"""

alph = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

f = open("input.txt", "r")

total_priority = 0
numLines= 0
numAnomlu = 0

def find_anomoly(sack1,sack2,sack3):
    for i in range(int(len(sack1))):
        for j in range(int(len(sack2))):
            if(sack1[i] == sack2[j]):
                for k in range(len(sack3)):
                    if sack1[i] == sack3[k]:
                        #print("Anomoly: ", sack1[i])
                        return sack1[i]


sacks = f.readlines()
for i in range(0,len(sacks),3):
    prio = 0
    sack1 = sacks[i].strip()
    sack2 = sacks[i+1].strip()
    sack3 = sacks[i+2].strip()
    anom = find_anomoly(sack1,sack2,sack3)
    if anom is not None:
        numAnomlu += 1
        prio += alph.find(anom)+1
    total_priority += prio
        
    #print(sack)
    numLines += 1
print(total_priority)
f.close()
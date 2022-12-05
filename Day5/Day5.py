# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 18:43:48 2022

@author: samsh

Advent of Code 2022 Day 5

"""

import re
from collections import deque
from itertools import islice

"""
Part1
"""
f = open("input.txt", "r")

stackTops = ""
initialStacks = True
stacks = []
for line in f:
    if(line.startswith(" 1")):
        initialStacks = False    
    elif(initialStacks):
        s = re.findall('... ?',line)
        if(stacks == []):
            for i in s:
                stacks.append(deque())
        for i in range(len(s)):
            s[i] = s[i].strip()
            if(s[i] != ""):
                stacks[i].appendleft(s[i][1:2])
    elif(line != "\n"):
        n, s1, s2 = re.findall('[0-9]+',line)
        s1 = int(s1)-1
        s2 = int(s2)-1
        for i in range(int(n)):
            if (stacks[s1]):
                stacks[s2].append(stacks[s1].pop())
for s in stacks:
    stackTops += s[-1]
#print(stacks)
print(stackTops)
f.close()

"""
Part 2
"""

f = open("input.txt", "r")

stackTops = ""
initialStacks = True
stacks = []
for line in f:
    if(line.startswith(" 1")):
        initialStacks = False    
    elif(initialStacks):
        s = re.findall('... ?',line)
        if(stacks == []):
            for i in s:
                stacks.append(deque())
        for i in range(len(s)):
            s[i] = s[i].strip()
            if(s[i] != ""):
                stacks[i].appendleft(s[i][1:2])
    elif(line != "\n"):
        n, s1, s2 = re.findall('[0-9]+',line)
        n = int(n)
        s1 = int(s1)-1
        s2 = int(s2)-1
        if (len(stacks[s1]))>=n:
            substack = stacks[s1]
            substack = list(substack)[len(substack)-n:]
            stacks[s2].extend(substack)
            newstack = stacks[s1]
            newstack = list(newstack)[:len(newstack)-n]
            stacks[s1]=deque(newstack)
            
for s in stacks:
    stackTops += s[-1]
#print(stacks)
print(stackTops)
f.close()
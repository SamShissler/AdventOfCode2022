# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 18:43:48 2022

@author: samsh

Advent of Code 2022 Day 5

"""

alph = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

f = open("input.txt", "r")

numOfContained = 0
numOfOverlapped = 0

for line in f:
    isContained = 0
    elf1, elf2 = line.strip().split(",")
    elf1L, elf1H = elf1.split("-")
    elf2L, elf2H = elf2.split("-")
    #print(elf1L,elf1H,elf2L,elf2H)
    if(int(elf1L) <= int(elf2L) and int(elf1H) >= int(elf2H)):
        #print("elf1 contains elf2")
        numOfContained += 1
        numOfOverlapped += 1
    elif(int(elf1L) >= int(elf2L) and int(elf1H) <= int(elf2H)):
        #print("elf2 contains elf1")
        numOfContained += 1
        numOfOverlapped += 1
    elif(int(elf1L) >= int(elf2L) and int(elf1L) <= int(elf2H)):
        numOfOverlapped += 1
    elif(int(elf2L)>=int(elf1L) and int(elf2L)<= int(elf1H)):
        numOfOverlapped += 1

print(numOfContained)
print(numOfOverlapped)
f.close()


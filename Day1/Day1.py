# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 00:40:12 2022

@author: samsh

Advent of Code 2022 Day 1

Calorie Counting

Part 1
Heaviest Elf

Part 2
Sum of heaviest 3 elves

"""

f = open("input.txt", "r")

heaviest_elf = 0
second = 0
third = 0
elf_weight = 0

for cal in f:
    if(cal == "\n" or cal == ""):
        if(elf_weight > third):
            if(elf_weight > second):
                if(elf_weight > heaviest_elf):
                    third = second
                    second = heaviest_elf
                    heaviest_elf = elf_weight
                else:
                    third = second
                    second = elf_weight
            else:
                third = elf_weight
        elf_weight = 0
    else:
        elf_weight += int(cal)
    print(elf_weight)
print("\n")
print(heaviest_elf)
print(heaviest_elf + second + third)
f.close()
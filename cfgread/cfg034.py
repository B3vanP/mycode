#!/usr/bin/env python3
## prompt the user for the name of the file to load
filename = input("Please enter the name of the file to load: ")

## create file object in "r"ead mode
with open(filename, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()

## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)
print(len(configlist))  # This line displays the number of lines


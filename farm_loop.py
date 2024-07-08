#!/usr/bin/env python3
"""
This script performs the following tasks:
1. Prints each animal from the NE Farm.
2. Asks the user to choose a farm and returns the plants/animals raised on that farm.
3. Asks the user to choose a farm and returns only the animals from that particular farm.
"""

# Farm data
farms = [
    {"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
    {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
    {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}
]

# Task 1: Print each animal from the NE Farm
print("Animals on the NE Farm:")
for item in farms[0]['agriculture']:
    if item not in ["carrots", "celery"]:
        print(item)
print()

# Task 2: Ask a user to choose a farm and return the plants/animals that are raised on that farm
farm_names = {farm["name"] for farm in farms}

def choose_farm():
    print("Choose a farm (NE Farm, W Farm, or SE Farm):")
    farm_choice = input()
    while farm_choice not in farm_names:
        print("Invalid choice. Please choose a valid farm (NE Farm, W Farm, or SE Farm):")
        farm_choice = input()
    return farm_choice

farm_choice = choose_farm()
for farm in farms:
    if farm["name"] == farm_choice:
        print(f"Plants/Animals on the {farm_choice}: {', '.join(farm['agriculture'])}")
print()

# Task 3: Ask a user to choose a farm but only return ANIMALS from that particular farm
farm_choice = choose_farm()
for farm in farms:
    if farm["name"] == farm_choice:
        animals = [item for item in farm["agriculture"] if item not in ["carrots", "celery"]]
        print(f"Animals on the {farm_choice}: {', '.join(animals)}")


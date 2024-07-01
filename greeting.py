#!/usr/bin/python3
def greet_user():
    name = input("Please enter your name: ").strip()
    day_of_week = input("Please enter the day of the week: ").strip().capitalize()
    
    print(f"Hello, {name}! Happy {day_of_week}!")

greet_user()


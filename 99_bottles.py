#!/usr/bin/env python3
"""
This script prints the lyrics to the song "99 Bottles of Beer on the Wall".
The user can input a starting number of bottles, up to a maximum of 100.
"""

def sing_99_bottles():
    while True:
        try:
            start_bottles = int(input("Enter the number of bottles to start with (maximum 100): "))
            if 0 < start_bottles <= 100:
                break
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")

    for i in range(start_bottles, 0, -1):
        if i > 1:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print(f"Take one down and pass it around, {i-1} {'bottles' if i-1 > 1 else 'bottle'} of beer on the wall.\n")
        else:
            print(f"{i} bottle of beer on the wall, {i} bottle of beer.")
            print(f"Take one down and pass it around, no more bottles of beer on the wall.\n")
    
    print("No more bottles of beer on the wall, no more bottles of beer.")
    print("Go to the store and buy some more, 99 bottles of beer on the wall.")

if __name__ == "__main__":
    sing_99_bottles()


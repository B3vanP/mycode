#!/usr/bin/env python3

"""
pokemon_info.py

This script allows the user to input a number between 1 and 151, corresponding to the original 151 Pokemon.
It retrieves information about the selected Pokemon from the PokeAPI, including:
1. The URL to the "front_default" sprite (an image of the Pokemon).
2. The names of a few moves the Pokemon can learn, summarizing the rest.
3. The total number of games the Pokemon has appeared in.

Usage:
    Run the script and follow the prompt to enter a number between 1 and 151.
"""

import requests

def get_pokemon_info():
    pokenum = input("Pick a number between 1 and 151!\n>")
    pokeapi = requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

    # Print the URL to the "front_default" sprite
    sprite_url = pokeapi['sprites']['front_default']
    print(f"Sprite URL: {sprite_url}")

    # Print out the names of a few of the selected Pokemon's moves and summarize the rest
    print("Moves:")
    moves = [move['move']['name'] for move in pokeapi['moves']]
    for move in moves[:5]:
        print(f"- {move}")
    if len(moves) > 5:
        print(f"...and {len(moves) - 5} more moves")

    # Count the total number of games this Pokemon character appeared in
    game_count = len(pokeapi['game_indices'])
    print(f"Total number of games: {game_count}")

def main():
    while True:
        get_pokemon_info()
        another = input("Would you like to pick another number? (yes/no)\n>").strip().lower()
        if another != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()


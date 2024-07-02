#!/usr/bin/env python3

def capitalize_name(name):
    return ' '.join([word.capitalize() for word in name.split()])

def get_character_info():
    marvelchars = {
        "Starlord": {
            "real name": "peter quill",
            "powers": "dance moves",
            "archenemy": "Thanos"
        },
        "Mystique": {
            "real name": "raven darkholme",
            "powers": "shape shifter",
            "archenemy": "Professor X"
        },
        "Hulk": {
            "real name": "bruce banner",
            "powers": "super strength",
            "archenemy": "adrenaline"
        }
    }

    while True:
        char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk): ").title()
        char_stat = input("What statistic do you want to know about? (real name, powers, archenemy): ").lower()

        if char_name in marvelchars and char_stat in marvelchars[char_name]:
            value = marvelchars[char_name][char_stat]
            if char_stat == "real name":
                value = capitalize_name(value)
            print(f"{char_name}'s {char_stat} is: {value}")
        else:
            print("Invalid input, please try again.")

        try_again = input("Do you want to try again? (yes or no): ").lower()
        if try_again != 'yes':
            break

get_character_info()


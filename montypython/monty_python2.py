#!/usr/bin/env python3

# counter loop start number
round = 0
# start of while loop
while True:
    # counter variable
    round = round + 1
    # question on the screen
    print('Finish the movie title, "Monty Python\'s The Life of ______"')
    # request answer from user
    answer = input("Your guess--> ")
    # check user input
    if answer == 'Brian':
        print('Correct')
        # break statement escapes the while loop
        break
    # logic to ensure round has not yet reached 3
    elif round==3:
        print("Sorry, the answer was Brian.")
        # break statement excapes the while loop
        break
    # if answer was wrong, and round is not yet equal to 3
    else:
        print("Sorry! Try again!")

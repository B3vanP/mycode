#!/usr/bin/env python3

import html
import random

# Trivia dictionary
trivia = {
    "category": "Entertainment: Film",
    "type": "multiple",
    "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
    "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
    "incorrect_answers": [
        "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
        "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
        "&quot;Round up the usual suspects.&quot;"
    ]
}

# Function to display the question and answers
def display_trivia(trivia):
    question = html.unescape(trivia["question"])
    correct_answer = html.unescape(trivia["correct_answer"])
    incorrect_answers = [html.unescape(ans) for ans in trivia["incorrect_answers"]]

    # Combine correct and incorrect answers
    all_answers = incorrect_answers + [correct_answer]

    # Shuffle the answers
    random.shuffle(all_answers)

    # Create a mapping from A, B, C, D to answers
    answer_mapping = {chr(65+i): ans for i, ans in enumerate(all_answers)}

    print("Question: ", question)
    for key, answer in answer_mapping.items():
        print(f"{key}: {answer}")

    return answer_mapping, correct_answer

# Function to get the user's answer and check if it is correct
def check_answer(answer_mapping, correct_answer):
    user_answer = input("Enter your answer (A, B, C, or D): ").upper()
    
    if user_answer in answer_mapping:
        if answer_mapping[user_answer] == correct_answer:
            print("Correct!")
        else:
            print("Incorrect. The correct answer is:", correct_answer)
    else:
        print("Invalid answer. Please enter A, B, C, or D.")

# Main function to run the trivia
def main(trivia):
    answer_mapping, correct_answer = display_trivia(trivia)
    check_answer(answer_mapping, correct_answer)

# Run the trivia
if __name__ == "__main__":
    main(trivia)


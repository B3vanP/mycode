#!/usr/bin/env python3

"""
This script determines your Myers-Briggs Type Indicator (MBTI) personality type
based on your answers to four questions. Each question corresponds to one of the
four dichotomies in the MBTI framework:
1. Extraversion (E) or Introversion (I)
2. Sensing (S) or Intuition (N)
3. Thinking (T) or Feeling (F)
4. Judging (J) or Perceiving (P)

The program validates user input, ensuring only valid choices are accepted.
After all inputs are collected, it constructs and displays your MBTI type along
with a brief description of your personality.
"""

def get_input(prompt, valid_inputs):
    while True:
        try:
            value = input(prompt).strip().upper()
            if value not in valid_inputs:
                raise ValueError(f"Invalid input. Please choose from {valid_inputs}.")
            return value
        except ValueError as e:
            print(e)

def main():
    print("Welcome to the Myers-Briggs Type Indicator (MBTI) Personality Test!")
    print("Please answer the following questions to determine your personality type.")
    
    ei = get_input("Do you prefer (E)xtraversion or (I)ntroversion? (E/I): ", ['E', 'I'])
    sn = get_input("Do you prefer (S)ensing or i(N)tuition? (S/N): ", ['S', 'N'])
    tf = get_input("Do you prefer (T)hinking or (F)eeling? (T/F): ", ['T', 'F'])
    jp = get_input("Do you prefer (J)udging or (P)erceiving? (J/P): ", ['J', 'P'])

    mbti_type = ei + sn + tf + jp
    
    print(f"Your MBTI personality type is: {mbti_type}")

    personality_descriptions = {
        "ESTJ": "The Executive: Organized, group oriented, focused on tasks.",
        "ISTJ": "The Inspector: Responsible, meticulous, detail-oriented.",
        "ESFJ": "The Caregiver: Warm-hearted, popular, and conscientious.",
        "ISFJ": "The Protector: Caring, dedicated, and very protective.",
        "ESTP": "The Entrepreneur: Energetic, lively, and fun-loving.",
        "ISTP": "The Virtuoso: Bold, practical, and good with hands.",
        "ESFP": "The Performer: Enthusiastic, friendly, and spontaneous.",
        "ISFP": "The Artist: Gentle, sensitive, and artistic.",
        "ENTJ": "The Commander: Bold, imaginative, and strong-willed.",
        "INTJ": "The Architect: Innovative, strategic, and logical.",
        "ENTP": "The Debater: Smart, curious, and open-minded.",
        "INTP": "The Thinker: Innovative, curious, and logical.",
        "ENFJ": "The Protagonist: Charismatic, inspiring, and natural leader.",
        "INFJ": "The Advocate: Idealistic, organized, and insightful.",
        "ENFP": "The Campaigner: Enthusiastic, creative, and sociable.",
        "INFP": "The Mediator: Empathetic, idealistic, and deeply reflective."
    }

    if mbti_type in personality_descriptions:
        print(personality_descriptions[mbti_type])
    else:
        print("Error: Unexpected MBTI type. Please check your input.")

if __name__ == "__main__":
    main()


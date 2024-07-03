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

def get_preference(prompt):
    while True:
        preference = input(prompt).strip().upper()
        if preference in ['E', 'I', 'S', 'N', 'T', 'F', 'J', 'P']:
            return preference
        else:
            print("Invalid input. Please enter a valid choice.")

def main():
    print("Welcome to the Myers-Briggs Type Indicator (MBTI) Personality Test!")
    print("Please answer the following questions to determine your personality type.")
    
    ei = get_preference("Do you prefer (E)xtraversion or (I)ntroversion? (E/I): ")
    sn = get_preference("Do you prefer (S)ensing or i(N)tuition? (S/N): ")
    tf = get_preference("Do you prefer (T)hinking or (F)eeling? (T/F): ")
    jp = get_preference("Do you prefer (J)udging or (P)erceiving? (J/P): ")

    mbti_type = ei + sn + tf + jp
    
    print(f"Your MBTI personality type is: {mbti_type}")

    if mbti_type == "ESTJ":
        print("The Executive: Organized, group oriented, focused on tasks.")
    elif mbti_type == "ISTJ":
        print("The Inspector: Responsible, meticulous, detail-oriented.")
    elif mbti_type == "ESFJ":
        print("The Caregiver: Warm-hearted, popular, and conscientious.")
    elif mbti_type == "ISFJ":
        print("The Protector: Caring, dedicated, and very protective.")
    elif mbti_type == "ESTP":
        print("The Entrepreneur: Energetic, lively, and fun-loving.")
    elif mbti_type == "ISTP":
        print("The Virtuoso: Bold, practical, and good with hands.")
    elif mbti_type == "ESFP":
        print("The Performer: Enthusiastic, friendly, and spontaneous.")
    elif mbti_type == "ISFP":
        print("The Artist: Gentle, sensitive, and artistic.")
    elif mbti_type == "ENTJ":
        print("The Commander: Bold, imaginative, and strong-willed.")
    elif mbti_type == "INTJ":
        print("The Architect: Innovative, strategic, and logical.")
    elif mbti_type == "ENTP":
        print("The Debater: Smart, curious, and open-minded.")
    elif mbti_type == "INTP":
        print("The Thinker: Innovative, curious, and logical.")
    elif mbti_type == "ENFJ":
        print("The Protagonist: Charismatic, inspiring, and natural leader.")
    elif mbti_type == "INFJ":
        print("The Advocate: Idealistic, organized, and insightful.")
    elif mbti_type == "ENFP":
        print("The Campaigner: Enthusiastic, creative, and sociable.")
    elif mbti_type == "INFP":
        print("The Mediator: Empathetic, idealistic, and deeply reflective.")
    else:
        print("Error: Unexpected MBTI type. Please check your input.")

if __name__ == "__main__":
    main()


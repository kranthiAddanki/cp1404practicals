"""
CP1404/CP5632 - Practical 2
score program
"""


# def main():
#     score = float(input("Enter score: "))
#     print(calculate_result(score))
#
# def calculate_result(score):
#     if score < 0 or score > 100:
#         return "Invalid score"
#     elif score >= 90:
#         return "Excellent"
#     elif score >= 50:
#         return "pass"
#     else:
#         return "Bad"


# main()

# Version_2

import random

def main():
# randomise score
    score = random.randint(1,100)
    print(score)
    print(calculate_result(score))

def calculate_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "pass"
    else:
        return "Bad"


main()
"""
https://github.com/CP1404/Practicals/tree/master/prac_04
"""

import random
NUMBERS_FOR_LINE = 6
MAXIMUM = 45
MINIMUM = 1

number_of_quick_picks = int(input("How many quick picks would you like to generate? "))
for i in range (number_of_quick_picks):
      quick_pick = []
      for j in range (NUMBERS_FOR_LINE) :
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                  number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
      quick_pick.sort()
      print(" " .join(f"{number:2}"for number in quick_pick))



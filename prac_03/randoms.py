"""
import random

print(random.randint(5, 20))
print(random.randrange(3, 10, 2))
print(random.uniform(2.5, 5.5))
"""

# What did you see on line 1?
# What was the smallest number you could have seen, what was the largest?
# 9and 20 ( 5 could be the smallest number)

# What did you see on line 2?
# What was the smallest number you could have seen, what was the largest?
# 3 and 9
# Could line 2 have produced a 4?
# No
# What did you see on line 3?
# What was the smallest number you could have seen, what was the largest?
# any float number between 2.5  and 3.5 inclusive
# Write code, not a comment, to produce a random number between 1 and 100 inclusive.

import random
# version_1
print(random.randrange(1,101))
#version_2: randint is inclusive of the both upper and lower bounds
print(random.randint(1,100))
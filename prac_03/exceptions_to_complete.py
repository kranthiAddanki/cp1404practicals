"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""


#Version_1
# is_finished = False
# while not is_finished:
#     try:
#         result = int(input("Enter a valid integer: "))
       # TODO: this line
#     except:  # TODO - add the exception you want to catch after except
#         print("Please enter a valid integer.")
# print("Valid result is:", result)

#version_2
is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)
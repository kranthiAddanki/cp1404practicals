"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    try:
        fraction = numerator / denominator
    except ZeroDivisionError:
        pass
#    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# Questions
# When will a ValueError occur?
# when a non-numeric or string is passed in the place which is expecting a number
# When will a ZeroDivisionError occur?
# when some number is divided by zero
# Could you change the code to avoid the possibility of a ZeroDivisionError?

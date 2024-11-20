"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

# sales = float(input("Enter sales: $"))
# if sales < 1000:
#     bonus = (10 / 100) * sales
# else:
#     bonus = (15 / 100) * sales
#     print("Your bonus is:", bonus)
#     sales = float(input("Enter sales: $"))

"""
add a loop to this, so it repeatedly asks for the user's sales 
and prints the bonus until they enter a negative number.
"""

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = (10 / 100) * sales
    else :
        bonus = (15 / 100) * sales
    print("Your bonus is:", bonus)
    sales = float(input("Enter sales: $"))
print("Thank you!")


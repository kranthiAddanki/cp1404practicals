"""
The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total
before the amount is displayed on the screen.
"""

# number_of_items = int(input("Enter the number of items: "))
# total_price = 0
# for i in range(1, number_of_items + 1):
#     item_price = float(input(f"Enter the item price {i}: "))
#     total_price += item_price
# if total_price > 100:
#     total_price = total_price - (total_price * 0.1)
# print(f"Total price for {number_of_items} items: {total_price:.2f}")

"""
If the number of items is less than zero, the message "Invalid number of items!" 
should be displayed and this quantity must be re-entered by the user until it is valid.
"""

number_of_items = int(input("Enter the number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Enter the number of items: "))
total_price = 0
for i in range(1, number_of_items+1):
    item_price = float(input(f"Enter the item price {i}: "))
    total_price += item_price
if total_price > 100:
    total_price = total_price - (total_price * 0.1)
print(f"Total price for {number_of_items} items: $ {total_price:.2f}")


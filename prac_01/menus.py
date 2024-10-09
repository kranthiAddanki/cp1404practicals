"""
menus program from https://github.com/CP1404/Practicals/tree/master/prac_01
"""

name = input("Enter your name: ")
menu = "(H)ello\n(G)oodbye\n(Q)uit"
print(menu)
choice = input("Enter your choice: ").upper()
while choice != "Q":
   if choice == "H":
       print("hello", name)
   elif choice == "G":
      print("goodbye", name)
   else:
      print("invalid choice")
   print(menu)
   choice = input("Enter your choice: ").upper()
print("Finished")
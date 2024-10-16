

MENU = """(G)et a valid score
(P)print result
(S)how stars
(Q)Quit"""

print(MENU)


# from prac_01.broken_score import score_result

#
def main():
    menu()
    get_valid_score()
    score_result()
    print_stars()

def menu():  # need to write a menu of choices and then do the functions based ont the choices
    if

def get_valid_score():
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score

def print_stars():
    print(f"Your score is {score_result()}")
    print("*" * score_result())


main()

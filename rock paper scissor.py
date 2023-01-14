# rock paper scissor

import random

comp_score = user_score = 0


def comp_turn(a):
    x = random.randint(1, 3)
    print("        ", a, "<-->", x, "        ")
    result(a, x)


def result(a, x):
    global comp_score, user_score
    if a == 1:
        if x == 2:
            print("computer won")
            comp_score += 1
        elif x == 3:
            print("you won")
            user_score += 1
        else:
            print("tied")
    elif a == 2:
        if x == 1:
            print("you won")
            user_score += 1
        elif x == 3:
            print("computer won")
            comp_score += 1
        else:
            print("tied")
    elif a == 3:
        if x == 1:
            print("computer won")
            comp_score += 1
        elif x == 2:
            print("you won")
            user_score += 1
        else:
            print("tied")
    else:
        print("enter the correct choice")
        main()


def main():
    print("1- stone; ")
    print("2- paper; ")
    print("3- scissors; ")
    a = int(input("enter your choice"))
    comp_turn(a)
    ch = input("one more play? (y/n) ")
    if ch == "y":
        main()
    else:
        print("****** end Scores ******")
        print("Your Score: ", user_score, "\t Computer Score: ", comp_score)
        if user_score > comp_score:
            print("Congratulations ! You are the overall winner")
        elif comp_score > user_score:
            print("Better Luck Next time ! Computer is the overall winner")
        else:
            print("Played well ! Both you and computer tied")

main()

# Simple Arithmetic Exercise  by  Max Fischetti

from random import randint, choices
import os
from datetime import datetime

num_of_questions = 5

difficulty = "E"


def get_difficulty():
    diff = ""
    while (diff != "E") and (diff != "M") and (diff != "D"):
        os.system("cls")
        print(f"\nSIMPLE ARITHMETRIC EXERCISE\n")
        diff = input("HOW DIFFICULT (E-easy, M-medium, D- difficult): ").upper()
    return diff


def print_problem(num_of_questions, diff):
    correct_answers = 0
    for ques_num in range(1, num_of_questions + 1):
        num1 = randint(1, 9 + (10 if diff in ("M", "D") else 0))
        num2 = randint(1, 9 + (10 if diff == "D" else 0))
        oper = choices(["+", "-", "*"])[0]
        user = int(input(f"{ques_num}: {num1} {oper} {num2} = "))
        if user == eval(str(num1) + oper + str(num2)):
            print(f"CORRECT\n")
            correct_answers += 1
        else:
            print(f"INCORRECT\n")
    return f"You correctly answered {correct_answers} out of {num_of_questions}"


init_time = datetime.now()

difficulty = get_difficulty()
print(print_problem(num_of_questions, difficulty), end=" in ")

end_time = datetime.now()

print(f"{(end_time - init_time).total_seconds():.2f} seconds")


print("\n" * 3)

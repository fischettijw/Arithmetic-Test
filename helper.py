import random
import os
from datetime import datetime

num_of_questions = 5

def print_heading(diff):
    os.system("cls")
    print("\nSIMPLE ARITHMETRIC EXERCISE", end="")
    if diff == "E":
        print(" - DIFFICULTY EASY\n")
    if diff == "M":
        print(" - DIFFICULTY MEDIUM\n")
    if diff == "H":
        print(" - DIFFICULTY HARD\n")


def get_difficulty():
    diff = ""
    while diff not in ("E", "M", "H"):
        os.system("cls")
        diff = input("HOW DIFFICULT (E-easy, M-medium, H- hard): ").upper()
    return diff


def get_numbers(diff):
    if diff == "E":
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
    if diff == "M":
        num1 = random.randint(10, 99)
        num2 = random.randint(0, 9)
    if diff == "H":
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
    return num1, num2


def print_problems(num_of_questions, diff):
    correct_answers = 0
    start_time = datetime.now()
    for ques_num in range(1, num_of_questions + 1):
        # num1 = random.randint(1, 9 + (10 if diff in ("M", "H") else 0))
        # num2 = random.randint(1, 9 + (10 if diff == "H" else 0))
        num1, num2 = get_numbers(diff)
        oper = random.choices(["+", "-", "*"])[0]
        user = int(input(f"{ques_num}: {num1} {oper} {num2} = "))
        if user == eval(str(num1) + oper + str(num2)):
            print(f"CORRECT\n")
            correct_answers += 1
        else:
            print(f"INCORRECT\n")
    end_time = datetime.now()
    print(f"You correctly answered {correct_answers} out of {num_of_questions} questions in ", end = "")
    print(f"{(end_time - start_time).total_seconds():.2f} seconds\n")


difficulty = get_difficulty()
print_heading(difficulty)
print_problems(num_of_questions,difficulty)


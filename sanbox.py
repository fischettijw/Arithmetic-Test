# Simple Arithmetic Exercise  by  Max Fischetti

import random
import os

diff = ""

while (diff != "E") and (diff != "M") and (diff != "D"):
    os.system("cls")
    diff = input("HOW DIFFICULT (E-easy, M-medium, D- difficult): ").upper()

print(f"\nSIMPLE ARITHMETRIC EXERCISE ({diff})\n")

questions = 1

while questions <= 10:

    if diff == 'E':
        # diff_level = "EASY"
        num1 = random.randint(0,9)
        num2 = random.randint(0,9)

    if diff == 'M':
        # diff_level = "MEDIUM"
        num1 = random.randint(0,99)
        num2 = random.randint(0,9)
        
    if diff == 'D':
        # diff_level = "DIFFICULT"
        num1 = random.randint(0,99)
        num2 = random.randint(0,99)

    operation = random.choices(["+", "-", "*"])
    
    if operation[0] == "+":
        answer = num1 + num2

    if operation[0] == "-":
        answer = num1 - num2
        
    if operation[0] == "*":
        answer = num1 * num2
            
    print(questions, ":",num1, operation[0], num2, "=", answer)
    questions +=1







print('\n\n\n\n\n')
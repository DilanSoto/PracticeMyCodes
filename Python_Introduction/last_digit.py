#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = number % 10

print(f"the last digit of", number, "is", lastDigit, end=" ")

if lastDigit > 5:
    print("greater than 5")
elif lastDigit == 0:
        print("and is 0")
elif lastDigit < 6:
    print("and is less than 6 and not 0")
    
    
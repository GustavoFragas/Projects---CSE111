"""
Program
Write a Python program named random_numbers.py that creates a list of numbers, appends more numbers onto the list, and prints the list. The program must have two functions named main and append_random_numbers as follows:

Requirements
Your program includes two functions named main and append_random_numbers. The append_random_numbers function has two parameters named numbers_list and quantity, and quantity has a default value of 1.
The main function calls append_random_numbers twice, first with one argument and second with two arguments.
The append_random_numbers function includes a loop that appends quantity random numbers at the end of numbers_list.
"""

import random
import os

def main():
    numbers = [1, 2, 3]
    random_words = ["apple", "banana", "cherry", "date", "elderberry"]

    print("We have a D20 dice to roll for you.")
    print("If you roll more than 13, you have the privilege to add random numbers and words to the lists.")
    lucky = input("Do you want to play this game? (y/n) ")

    while lucky.lower() not in ['y', 'n']:
        os.system('cls' if os.name == 'nt' else 'clear')
        lucky = input("Invalid input. Please enter 'y' or 'n': ")

    if lucky.lower() == 'y':
        roll = rolling_d20()
        print(f"You rolled a {roll}.")
        if roll > 13:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Your roll is {roll}")
            print("Congratulations!")
            print("You can add random numbers and words to the lists.")
        else:
            print("Sorry, you cannot add random numbers and words to the lists.")
            return
    
    elif lucky.lower() == 'n':
        print("Maybe next time!")
        return

    
    qtd = int(input("How many random numbers do you want to add? "))
    append_random_numbers(numbers)
    append_random_numbers(numbers, qtd)
    append_random_words(random_words)
    append_random_words(random_words, qtd)
    print(numbers)
    print(random_words)

def rolling_d20():
    return random.randint(1, 20)

def append_random_numbers(numbers_list, quantity = 1):
    for line in range(quantity):
        numbers_list.append(random.randint(1, 100))

def append_random_words(words_list, quantity = 1):
    for line in range(quantity):
        words_list.append(random.choice(["fig", "grape", "honeydew", "kiwi", "lemon"]))

if __name__ == "__main__":
    main()
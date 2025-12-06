import os
import random
import datetime
import time

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    welcome_message()   
    
    while True:
        language = input("Type 'E' for English or 'P' for Portuguese(Escreva 'E' para Inglês ou 'P' para Português):\n> ").strip().upper()

        if language_validator(language):
            break
    
    if language == "E":
        main_english()
    
    elif language == "P":
        main_portuguese()
    

def welcome_message():
        
        print("Welcome to the Gym Rat")
        print("Bem vindo ao Gym Rat")

        print()

        print("Before starting, to have a better experience, please inform us about your language preference.")
        print("Antes de começar, para ter uma melhor experiência, por favor nos informe sua preferência de idioma.")
            
        print()    

# Validate language input
def language_validator(language):
        
    if language not in ["E", "P"]:
        os.system('cls' if os.name == 'nt' else 'clear')

        welcome_message()
        print("Invalid input. Please type 'E' for English or 'P' for Portuguese.")
        print("Entrada inválida. Por favor, digite 'E' para Inglês ou 'P' para Português.")
        
        return False
    return True
        
def main_english():

    word_effect("You have selected English.")
    os.system('cls' if os.name == 'nt' else 'clear')
    word_effect("Light weight, BABYYY!")
    word_effect("-Ronnie Coleman", delay=0.01)
    print()

    print("Log in to your account to continue.")

    print("1 - Log In\n2 - Sign Up\n3 - Exit")


def main_portuguese():

    word_effect("Você selecionou Português.")
    os.system('cls' if os.name == 'nt' else 'clear')
    word_effect("O shape fala por mim!")
    word_effect("-Toguro", delay=0.01)
    print()
    pass

def word_effect(word, delay=0.05):
    for char in word:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

if __name__ == "__main__":
    main()
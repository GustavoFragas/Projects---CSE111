import os
import time
import json

script_dir = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(script_dir, "username_passwords.txt")

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

def language_validator(language): 
    if language not in ["E", "P"]:
        os.system('cls' if os.name == 'nt' else 'clear')
        welcome_message()
        print("Invalid input. Please type 'E' for English or 'P' for Portuguese.")
        print("Entrada inválida. Por favor, digite 'E' para Inglês ou 'P' para Português.")
        return False
    return True
        
def main_english():
    choice = ""
    word_effect("You have selected English.")
    os.system('cls' if os.name == 'nt' else 'clear')
    word_effect("Light weight, BABYYY!")
    word_effect("-Ronnie Coleman", delay=0.01)
    print()

    print("Log in to your account to continue.")
    
    while choice != "3":
        print("1 - Log In\n2 - Sign Up\n3 - Exit")
        choice = input("> ").strip()
        os.system('cls' if os.name == 'nt' else 'clear')
        
        if not choice_validator(choice, "eng"):
            continue

        word_effect("You selected option " + choice)

        if choice == "1":
            current_user = choice_1()

            if current_user:
                home_page(current_user)
   
        elif choice == "2":
            choice_2()  
                    
        elif choice == "3":
            word_effect("Exiting the program. Goodbye!")
            exit()

def main_portuguese():
    pass

def choice_1():
            word_effect("Logging in...")
            
            word_effect("Light weight, BABYYY!")
            word_effect("-Ronnie Coleman", delay=0.01)
            print()
            if os.path.exists(DB_FILE):
                with open(DB_FILE, "r") as f:
                    try:
                        database = json.load(f)
                    except json.JSONDecodeError:
                        database = {}
            else:
                word_effect("No users registered yet. Please Sign Up first.")
                return
            
            while True:
                word_effect("Please enter your username and password to log in.")
                name = input("Username: ")
                password = input("Password: ")

                if name in database and database[name] == password:
                    word_effect(f"Login successful! Welcome back, {name}!")
                    return name
                
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    word_effect("Invalid username or password.")

def choice_2():
            word_effect("Signing up...")
            
            name = input("Enter your name: ")
            
            if os.path.exists(DB_FILE):
                try:
                    with open(DB_FILE, "r") as f:
                        content = f.read()
                        if content:
                            database = json.loads(content)
                        else:
                            database = {}
                except:
                    database = {}
            else:
                database = {}

            if name in database:
                word_effect("Username already exists. Try logging in.")
                return

            while True:
                password = input("Create a password: ")
                password_confirm = input("Confirm your password: ")
                
                if password == password_confirm:
                    database[name] = password
                    
                    with open(DB_FILE, "w") as f:
                        json.dump(database, f, indent=4)
                    
                    os.system('cls' if os.name == 'nt' else 'clear')
                    word_effect(f"Account created successfully!")
                    break
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    word_effect("Passwords do not match. Please try again.")

def word_effect(word, delay=0.05):
    for char in word:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def choice_validator(choice, language, valid_choices = ["1", "2", "3"]):
    if language == "eng":
        if choice not in valid_choices:
            word_effect("Invalid option. Please select a valid option.")
            return False
    elif language == "pt":
        if choice not in valid_choices:
            word_effect("Opção inválida. Por favor, selecione uma opção válida.")
            return False
    return True

def home_page(user):
    os.system('cls' if os.name == 'nt' else 'clear')
    word_effect(f"Welcome to your home page, {user}!")
    word_effect("You can now access the Gym Rat features.")
    print("1 - View Workout Plans\n2 - Log Workout\n3 - View Progress\n4 - Log Out")
    home_choice = input("> ").strip()
    os.system('cls' if os.name == 'nt' else 'clear')
    word_effect(f"You selected option {home_choice}. (Feature under development)")
    
if __name__ == "__main__":
    main()
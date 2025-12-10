import os
import time
import json
import datetime
import random

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
        print()
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
    choice = ""
    word_effect("Você selecionou Português.")
    os.system('cls' if os.name == 'nt' else 'clear')
    word_effect("O shape fala por mim!")
    word_effect("-Toguro", delay=0.01)
    print()

    print("Faça login na sua conta para continuar.")
    
    while choice != "3":
        print("1 - Entrar\n2 - Cadastrar\n3 - Sair")
        choice = input("> ").strip()
        os.system('cls' if os.name == 'nt' else 'clear')
        
        if not choice_validator(choice, "pt"):
            continue

        word_effect("Você selecionou a opção " + choice)

        if choice == "1":
            current_user = choice_1_pt()

            if current_user:
                home_page_pt(current_user)
   
        elif choice == "2":
            choice_2_pt()  
                    
        elif choice == "3":
            word_effect("Saindo do programa. Até logo!")
            exit()

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

        if name in database and database[name]['password'] == password:
            word_effect(f"Login successful! Welcome back, {name}!")
            return name
        
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            word_effect("Invalid username or password.")

def choice_1_pt():
    word_effect("Entrando...")
    word_effect("O shape fala por mim!")
    word_effect("-Toguro", delay=0.01)
    print()
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            try:
                database = json.load(f)
            except json.JSONDecodeError:
                database = {}
    else:
        word_effect("Nenhum usuário registrado ainda. Por favor, cadastre-se primeiro.")
        return
    
    while True:
        word_effect("Por favor, digite seu usuário e senha para entrar.")
        name = input("Usuário: ")
        password = input("Senha: ")

        if name in database and database[name]['password'] == password:
            word_effect(f"Login realizado com sucesso! Bem-vindo de volta, {name}!")
            return name
        
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            word_effect("Usuário ou senha inválidos.")

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
        os.system('cls' if os.name == 'nt' else 'clear')
        word_effect("Username already exists. Try logging in.")
        return

    while True:
        password = input("Create a password: ")
        password_confirm = input("Confirm your password: ")
        
        if password == password_confirm:
            database[name] = {
                "password": password,
                "plan": ""  
            }        

            with open(DB_FILE, "w") as f:
                json.dump(database, f, indent=4)
            
            os.system('cls' if os.name == 'nt' else 'clear')
            word_effect(f"Account created successfully!")
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            word_effect("Passwords do not match. Please try again.")

def choice_2_pt():
    word_effect("Cadastrando...")
    
    name = input("Digite seu nome: ")
    
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
        os.system('cls' if os.name == 'nt' else 'clear')
        word_effect("Nome de usuário já existe. Tente fazer login.")
        return

    while True:
        password = input("Crie uma senha: ")
        password_confirm = input("Confirme sua senha: ")
        
        if password == password_confirm:
            database[name] = {
                "password": password,
                "plan": ""  
            }        

            with open(DB_FILE, "w") as f:
                json.dump(database, f, indent=4)
            
            os.system('cls' if os.name == 'nt' else 'clear')
            word_effect(f"Conta criada com sucesso!")
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            word_effect("As senhas não coincidem. Tente novamente.")

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

def save_workout_log(username, workout_data):
    today_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            database = json.load(f)
        
        if username in database:
            if "logs" not in database[username]:
                database[username]["logs"] = {}
            
            database[username]["logs"][today_date] = workout_data
            
            with open(DB_FILE, "w") as f:
                json.dump(database, f, indent=4)

def generate_random_workout(workout_name, language="en"):
    file_name_map = {
        "en": {
            "back": "back_en.txt",
            "arms": "arms_en.txt",
            "chest": "chest_en.txt",
            "triceps": "arms_en.txt",
            "biceps": "arms_en.txt",
            "shoulders": "shoulders_en.txt",
            "legs": "legs_en.txt",
            "abs": "shoulders_en.txt"
        },
        "pt": {
            "back": "costas_br.txt",
            "arms": "braços_br.txt",
            "chest": "peito_br.txt",
            "triceps": "braços_br.txt",
            "biceps": "braços_br.txt",
            "shoulders": "ombros_br.txt",
            "legs": "pernas_br.txt",
            "abs": "ombros_br.txt"
        }
    }

    lang_key = "pt" if language.lower() in ["p", "pt", "br"] else "en"
    
    workout_recipes = {
        "Back and Biceps": [
            ("back", 5),
            ("arms", 3)
        ],
        "Chest and Triceps": [
            ("chest", 4), 
            ("arms", 3)
        ],
        "Shoulders and Abs": [
            ("shoulders", 5)
        ],
        "Legs": [
            ("legs", 6)
        ],

        "Push (Chest, Shoulders, Triceps)": [
            ("chest", 3),
            ("shoulders", 3),
            ("arms", 2)
        ],
        "Pull (Back, Biceps)": [
            ("back", 4),
            ("arms", 3)
        ],
        "Upper Body": [
            ("chest", 2), ("back", 2), ("shoulders", 2), ("arms", 2)
        ],
        "Lower Body": [
            ("legs", 6)
        ]
    }

    recipe = workout_recipes.get(workout_name)
    
    if not recipe:
        return []

    final_workout_list = []

    for concept, quantity in recipe:
        filename = file_name_map[lang_key].get(concept)
        
        if not filename:
            continue

        file_path = os.path.join(script_dir, "lista_exercicios", filename)

        if os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                    
                    if len(lines) > 1:
                        exercises_cleaned = [line.strip() for line in lines[1:] if line.strip()]
                        
                        count = min(len(exercises_cleaned), quantity)
                        selected = random.sample(exercises_cleaned, count)
                        
                        final_workout_list.extend(selected)
                        
            except Exception:
                pass

    return final_workout_list

def home_page(user):
    current_plan = ""
    
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            db = json.load(f)
            if user in db:
                current_plan = db[user].get('plan', "")

    os.system('cls' if os.name == 'nt' else 'clear')
    
    while True:
        word_effect(f"Welcome to your home page, {user}!")
        if current_plan:
             print(f"Current Plan: {current_plan}") 
        else:
             print("No workout plan logged yet.")
        
        word_effect("You can now access the Gym Rat features.")
        print("1 - View Workout Plans\n2 - Log/Change Workout Plan\n3 - View Progress\n4 - Log Out")

        home_choice = input("> ").strip()
        os.system('cls' if os.name == 'nt' else 'clear')

        if not choice_validator(home_choice, "eng", valid_choices=["1", "2", "3", "4"]):
            continue
        
        if home_choice == "1":
            if current_plan == "":
                word_effect("You have not logged any workouts yet. Please choose option 2 first.")
            else:
                home_choice_1(user, current_plan, language="en") 
            
        elif home_choice == "2":
            new_plan = home_choice_2()
            if new_plan:
                current_plan = new_plan 
                save_user_plan(user, current_plan) 
                word_effect("Plan saved successfully!")

        elif home_choice == "3":
            word_effect("Feature under development.")

        elif home_choice == "4":
            word_effect("Logging out...")
            break

def home_page_pt(user):
    current_plan = ""
    
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            db = json.load(f)
            if user in db:
                current_plan = db[user].get('plan', "")

    os.system('cls' if os.name == 'nt' else 'clear')
    
    while True:
        word_effect(f"Bem-vindo à sua página inicial, {user}!")
        if current_plan:
             print(f"Plano Atual: {current_plan}") 
        else:
             print("Nenhum plano registrado ainda.")
        
        word_effect("Você agora pode acessar as funções do Gym Rat.")
        print("1 - Ver Treinos\n2 - Registrar/Alterar Plano\n3 - Ver Progresso\n4 - Sair")

        home_choice = input("> ").strip()
        os.system('cls' if os.name == 'nt' else 'clear')

        if not choice_validator(home_choice, "pt", valid_choices=["1", "2", "3", "4"]):
            continue
        
        if home_choice == "1":
            if current_plan == "":
                word_effect("Você ainda não registrou nenhum treino. Por favor escolha a opção 2 primeiro.")
            else:
                home_choice_1(user, current_plan, language="pt") 
            
        elif home_choice == "2":
            new_plan = home_choice_2_pt()
            if new_plan:
                current_plan = new_plan 
                save_user_plan(user, current_plan) 
                word_effect("Plano salvo com sucesso!")

        elif home_choice == "3":
            word_effect("Função em desenvolvimento.")

        elif home_choice == "4":
            word_effect("Saindo...")
            break

def home_choice_1(user, train, language="en"):
    word_effect("Here is your workout plan:" if language == "en" else "Aqui está seu plano de treino:")
    today = datetime.datetime.now().weekday()
    name_today = datetime.datetime.now().strftime("%A")

    type_of_workout = training_plan_logger(today, train)
    
    if type_of_workout == "Rest Day":
        if language == "en":
            word_effect(f"Today is {name_today}. It's a Rest Day! Enjoy your recovery.")
        else:
            word_effect(f"Hoje é dia de descanso! Aproveite sua recuperação.")
        input("Press Enter to continue..." if language == "en" else "Pressione Enter para continuar...")
        return

    if language == "en":
        word_effect(f"Today is {name_today}. Focus: {type_of_workout}")
    else:
        word_effect(f"Foco de hoje: {type_of_workout}")
    print("------------------------------------------------")

    exercises = generate_random_workout(type_of_workout, language)

    if not exercises:
        word_effect("No exercises found for this workout." if language == "en" else "Nenhum exercício encontrado para este treino.")
        input("Press Enter to return..." if language == "en" else "Pressione Enter para voltar...")
        return

    for i, ex in enumerate(exercises, 1):
        print(f"{i}. {ex}")
    print("------------------------------------------------")

    while True:
        if language == "en":
            print("\nOptions: 1-Advice | 2-Log Weights | 3-Back")
        else:
            print("\nOpções: 1-Dicas | 2-Registrar Cargas | 3-Voltar")
        
        sub_choice = input("> ").strip()

        if sub_choice == "1":
            if language == "en":
                word_effect("Focus on technique. Control the eccentric phase.")
                print("press Enter to continue...")
                input()
                os.system('cls' if os.name == 'nt' else 'clear')

            else:
                word_effect("Foque na técnica. Controle a descida do peso.")
                print("pressione Enter para continuar...")
                input()
                os.system('cls' if os.name == 'nt' else 'clear')

        elif sub_choice == "2":
            if language == "en":
                word_effect("Type the weight (e.g., '20kg') or 'skip'.")
            else:
                word_effect("Digite o peso (ex: '20kg') ou 'pular'.")
            
            workout_log = {}
            for ex in exercises:
                print(f"{ex}:")
                weight = input("> ").strip()
                if weight.lower() not in ["skip", "pular", ""]:
                    workout_log[ex] = weight
            
            if workout_log:
                save_workout_log(user, workout_log)
                word_effect("Saved!" if language == "en" else "Salvo!")
                break
            else:
                word_effect("returning to menu." if language == "en" else "retornando ao menu.")
                print("press Enter to continue..." if language == "en" else "pressione Enter para continuar...")
                input()
                os.system('cls' if os.name == 'nt' else 'clear')
                break

        elif sub_choice == "3":
            break

def training_plan_logger(weekday, train):
    if train == "ABCD":
        if weekday == 0:
            return "Chest and Triceps"
        elif weekday == 1:
            return "Back and Biceps"
        elif weekday == 4:
            return "Shoulders and Abs"
        elif weekday == 5:
            return "Legs"
        else:
            return "Rest Day"
    if train == "PPL":
        if weekday == 0:
            return "Push (Chest, Shoulders, Triceps)"
        elif weekday == 1:
            return "Pull (Back, Biceps)"
        elif weekday == 2:
            return "Legs"
        elif weekday  == 4:
            return "Upper Body"
        elif weekday == 5:
            return "Lower Body" 
        else:
            return "Rest Day"

    if train == "UL":
        if weekday == 0:
            return "Upper Body"
        elif weekday == 1:
            return "Lower Body"
        elif weekday == 3:
            return "Upper Body"
        elif weekday == 4:
            return "Lower Body"
        else:
            return "Rest Day"

def home_choice_2():
    word_effect("Let's log your workout!")

    while True:
        print("Is your first time training? (Y/N)")
        first_time = input("> ").strip().upper()
        if first_time == "Y":
            word_effect("Perfect, let's set up a beginner workout plan for you!")
            word_effect("You will train 4 days a week, focusing on different muscle groups each day.")
            word_effect("Day 1: Chest and Triceps\nDay 2: Back and Biceps\nDay 3: rest\nDay 4: Shoulders and Abs\nDay 5: Legs\nDay 6: rest\nDay 7: rest")
            word_effect("Make sure to warm up before each session and cool down afterwards. Let's get started!")
            print("Press Enter to continue...")
            input()
            os.system('cls' if os.name == 'nt' else 'clear')
            train = "ABCD"
            return train

        elif first_time == "N":
            word_effect("Great! We have several workout plans available.")
            word_effect("1 - A B C D Split\n2 - Push Pull Legs\n3 - Upper Lower Split")
            while True:
                plan_choice = input("> ").strip()
                if plan_choice in ["1", "2", "3"]:
                    break
                else:
                    word_effect("Invalid choice. Please select a valid option.")
            os.system('cls' if os.name == 'nt' else 'clear')
            word_effect(f"You have selected plan {plan_choice}. Let's log your workout based on this plan!")
            if plan_choice == "1":
                train = "ABCD"
            elif plan_choice == "2":
                train = "PPL"
            elif plan_choice == "3":
                train = "UL"
            return train
        
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            word_effect("Invalid input. Please select another option.")

def home_choice_2_pt():
    word_effect("Vamos registrar seu plano de treino!")

    while True:
        print("É sua primeira vez treinando? (S/N)")
        first_time = input("> ").strip().upper()
        if first_time == "S":
            word_effect("Perfeito, vamos configurar um treino iniciante para você!")
            word_effect("Você treinará 4 dias por semana, focando em grupos musculares diferentes.")
            word_effect("Dia 1: Peito e Tríceps\nDia 2: Costas e Bíceps\nDia 3: Descanso\nDia 4: Ombros e Abdômen\nDia 5: Pernas\nDia 6: Descanso\nDia 7: Descanso")
            word_effect("Lembre-se de aquecer antes e alongar depois. Vamos começar!")
            print("Pressione Enter para continuar...")
            input()
            os.system('cls' if os.name == 'nt' else 'clear')
            train = "ABCD"
            return train

        elif first_time == "N":
            word_effect("Ótimo! Temos vários planos disponíveis.")
            word_effect("1 - Divisão A B C D\n2 - Push Pull Legs (Empurrar Puxar Pernas)\n3 - Upper Lower (Superior Inferior)")
            while True:
                plan_choice = input("> ").strip()
                if plan_choice in ["1", "2", "3"]:
                    break
                else:
                    word_effect("Escolha inválida. Selecione uma opção válida.")
            os.system('cls' if os.name == 'nt' else 'clear')
            word_effect(f"Você selecionou o plano {plan_choice}. Vamos registrar seu treino!")
            if plan_choice == "1":
                train = "ABCD"
            elif plan_choice == "2":
                train = "PPL"
            elif plan_choice == "3":
                train = "UL"
            return train
        
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            word_effect("Entrada inválida. Por favor selecione outra opção.")

def save_user_plan(username, plan):
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            database = json.load(f)
            
        if username in database:
            database[username]['plan'] = plan
            
            with open(DB_FILE, "w") as f:
                json.dump(database, f, indent=4)

if __name__ == "__main__":
    main()
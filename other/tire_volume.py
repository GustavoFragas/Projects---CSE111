"""
Gustavo Fragas Cunha
Ideas:

- Adding a menu for user interaction
- Implementing input validation for tire dimensions
- Using import os to clear the console on invalid input
- Using a loop to allow re-entry of values until valid input is received

"""

"""
Purpose:

Write a program that will accept user input that describes a tire then calculate and display the tire's volume. Record the tire information in a log file.
Have the user enter a tire width in mm.
Have the user enter the aspect ratio.
Have the user enter the diameter of the wheel in inches.
Calculate and display the tire's volume.
Log the information in a text file.
current date (Do NOT include time)
width of the tire
aspect ratio of the tire
diameter of the wheel
volume of the tire (rounded to two decimal places)

"""
"""
Answer example:
> python tire_volume.py
Enter the width of the tire in mm (ex 205): 185
Enter the aspect ratio of the tire (ex 60): 50
Enter the diameter of the wheel in inches (ex 15): 14
The approximate volume is 24.09 liters
> python tire_volume.py
Enter the width of the tire in mm (ex 205): 205
Enter the aspect ratio of the tire (ex 60): 60
Enter the diameter of the wheel in inches (ex 15): 15
The approximate volume is 39.92 liters
"""
import os
import math
from datetime import datetime

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    print("\nTire Volume Calculator")
    print("1. Calculate tire volume")
    print("2. View previous calculations")
    print("3. Exit")
    
    choice = input("\nChoose an option (1-3):\n>  ")
    
    if choice == "1":
        width = float(input("Enter the width of the tire in mm (ex 205): "))
        aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
        diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))
        
        if width <= 0 or aspect_ratio <= 0 or diameter <= 0:
            print("Error: All values must be positive, please")
            continue
            
        volume = math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter) / 10000000000
        
        base_cost = 50
        volume_cost = volume * 0.5
        total_cost = base_cost + volume_cost
        
        print(f"The approximate volume is {volume:.2f} liters")
        print(f"Estimated cost: ${total_cost:.2f}")
        
        # Esse escreve
        with open("tire_volumes.txt", "a") as log_file:
            current_date = datetime.now().strftime("%Y-%m-%d")
            log_file.write(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}, ${total_cost:.2f}\n")
            
    elif choice == "2":
        # esse abre e da o output pro cliente
        try:
            with open("tire_volumes.txt", "r") as file:
                print("\nPrevious calculations:")
                print("Date, Width(mm), Aspect Ratio, Diameter(in), Volume(L), Cost")
                print("-" * 65)
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print("No archive found.")
            
    elif choice == "3":
        print("Thank you for using Tire Volume Calculator")
        break
    
    else:
        print("Invalid option. Please try again.")





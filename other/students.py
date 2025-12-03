import csv
import os

"""
Background
A common task for many knowledge workers is to use a number, key, or ID to find information about a person. For example, a knowledge worker may use a phone number or e-mail address as a key to find (or look up) additional information about a customer. During this activity, your team will write a Python program that uses a student’s ID Number to look up the student’s name.

Program
This program will read data from a comma separated file (csv) of student information into a dictionary. This dictionary will then be used to lookup student information by ID number.

Requirements
Your program must do the following:

Open the students.csv file for reading, skip the first line of text in the file because it contains only headings, and read the other lines of the file into a dictionary. The program must store each student ID Number as a key and each ID Number name pair or each name as a value in the dictionary.
Get an ID Number from the user, use the ID Number to find the corresponding student name in the dictionary, and print the name.
If a user enters an ID Number that doesn’t exist in the dictionary, your program must print the message, "No such student" (without the quotes).
Enhancements
Here is a list of enhancements that you could make to the program. Your instructor will walk you through at least one of them. Feel free to complete others.

Add code to remove dashes from the ID Number that the user enters. This will allow the user to enter ID Numbers with dashes or without dashes and still allow the computer to search in the dictionary.
When a user enters an ID Number, your program should ensure it is a valid ID Number.
If there are too few digits in the ID Number, your program should print, "Invalid ID Number: too few digits" (without the quotes).
If there are too many digits in the ID Number, your program should print, "Invalid ID Number: too many digits" (without the quotes).
If the given ID Number contains any characters besides digits and dashes, your program should output "Invalid ID Number" (without the quotes).
Add something or change something in your program that you think would make your program better, easier for the user, more elegant, or more fun. Be creative.
"""

def main():
    students_diccionary = read_the_students_csv()
    
    name_of_the_student =  id_validator(students_diccionary)

    print (f"The name of the student is {name_of_the_student}") 


def read_the_students_csv():
    with open("students.csv", "rt", encoding="utf-8") as students_file:
        reader = csv.reader(students_file)
        next(reader)
        students_diccionary = {}
        for line in reader:
            students_diccionary[line[0]] = line[1]
    
    return students_diccionary

def id_validator(students_diccionary):
    id_length = 9
    while True:
         
        try:
            id_input = int(input("What's the ID? "))
            
            if len(str(id_input)) < id_length:
                print("Invalid ID Number: too few digits. An ID Number must have 9 digits.")
                continue

            if len(str(id_input)) > id_length:
                print("Invalid ID Number: too many digits. An ID Number must have 9 digits.")
                continue

            id_string = str(id_input) 

            return students_diccionary[id_string]
        
        except IndexError:
            print("Error: You must enter an ID Number.")

        except ValueError:
            print("Error: You must enter only numbers.Invalid ID Number.")
            
        except KeyError:
            print("No such student.")

if __name__ == "__main__":
    main()


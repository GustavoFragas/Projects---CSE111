"""
María García, from the security team has provided the following requirements and resources to help create the password strength checker.

The password checker should allow users to check passwords until they choose to quit. The hope is that by using the password checker tool employees will learn how to create better passwords.
Passwords should be checked against both a list of known passwords and a list of dictionary of words. María has provided both a dictionary file that contains about 70,000 words and a file that contains the top 1 million passwords used.
The tool will allow a user to enter a password, the tool will calculate the strength of the password (from 0 to 5), a message should be shown to inform the user the strength of the password.
María would like the strength calculator created as a function so it can be used in other future projects.
A passwords strength is calculated based on several factors including, is the password a dictionary word, is the password a known password, the length of the password and the complexity of the password. Here are the requirements:
If the password is in the dictionary file. (this should be a case insensitive match)
Print the message. "'Password is a dictionary word and is not secure."
Return a strength value of 0.
If the password is in the toppassword list. (this should be a case sensitive match)
Print the message "Password is a commonly used password and is not secure."
Return a strength value of 0
If the password is shorter than the minimum password length of 10
Print the message "Password is too short and is not secure."
Return a strength value of 1
If the password is longer than 15 characters, the password is strong
Print the message "Password is long, length trumps complexity this is a good password."
Return the strength value of 5
For the remainder of the cases the strength will be determined by the complexity of the password. Passwords are more difficult to crack if they contain multiple kinds of characters. For this program there are 4 kinds of characters, upper case letters, lower case letters, numeric digits, and special symbols. The complexity score is a number from 1 to 4 that indicates how many of the different types of characters are used in the password. E.g. if the password only had upper case characters it would have a complexity score of 1, if it had upper and lower case characters, it would have a complexity score of 2, etc.
The strength score will be calculated as a base score of 1 plus the complexity score.
Return the strength score.
Design
The requirements were sent to Sven Larson, one of our software architects, to provide design assistance with the program.

Sven and his team developed the following program architecture. Use this information to create your program. As a junior programmer, you must use the functions defined by Sven, you must use exact function names and parameters.

Function Specifications
Function Name	Parameters
Return Type	Description
word_in_file	Parameters
word,
filename,
case_sensitive

Return Tpe
Boolean	This function reads a file (specified by the filename parameter) in which each line of the file contains a single word. If the word passed in the word parameter matches a word in the file the function returns a true otherwise it returns a false. If the parameter case_sensitive is true a case sensitive match is performed. If case_sensitive is false a case insensitive match is performed. The case_sensitive parameter should default to False
word_has_character	Parameters
word,
character_list

Return Tpe
Boolean	This function loops through each character in the string passed in the word parameter to see if that character is in the list of characters passed in the character_list parameter. If any of the characters in the word are present in the character list return a true, If none of the characters in the word are in the character list return false
word_complexity	Parameters
word

Return Tpe
Integer	This function creates a numeric complexity value based on the types of characters the word parameter contains. One point of complexity is given for each type of character in the word. The function calls the word_has_character function for each of the 4 kinds of characters (LOWER, UPPER, DIGITS, SPECIAL). If the word has that kind of character a point is added to complexity rating. Since there are 4 kinds of characters the complexity rating will range from 0 to 4. (0 would be returned only if word contained no characters or only contains characters that are not in any of the lists.)
password_strength	Parameters
password,
min_length,
strong_length

Return Tpe
Integer	This function checks length requirements, checks dictionary and known-passwords, calls word_complexity to calculate the word's complexity then determines the password's strength based on the user requirements. It should print the messages defined in the requirements and return the password's strength as a number from 0 to 5. The min_length parameter should have a default value of 10. The strong_length parameter should have a default value of 16
main		Provides the user input loop. The loop asks the user for a password to test. If that password is anything but "q" or "Q" call the password_strength function and report the results to the user. If the u
ser enters "q" or "Q", quit the program.
Other helpful information.
Sven is aware that you are a junior programmer and offered a few tips to help you.

Include the following python code at the bottom of your program, this code will help the testing team ensure your program runs correctly. Sven has scheduled training for your team to introduce you to software testing in the near future.
if __name__ == "__main__":
    main()
Copy
When you open the password and dictionary files make sure you include the encoding parameter and pass it the value utf-8. This will ensure python knows how to read the file properly.
open(filename, "r",encoding="utf-8")
Copy
When you read a line from the file, use the strip() function of the string to remove the newline character from the end of the string. If you don't your word comparisons will not return the expected result.
You may use the following definitions for the lists of character types
LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "\"", "\"", ",", ".", "<", ">", "?", "/", "`", "~"]
"""
"""
Gustavo Fragas Cunha

My creativity and knowledge applied to code.
- I used import os to clear the screen between password checks
- I used try and except to handle file not found errors 
- I did a if password == "": to avoid empty passwords

Today is November 06, 2025
"""

import math
import os


LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", """, """, ",", ".", "<", ">", "?", "/", "`", "~"]

def main():
    print("Welcome to the Password Strength Checker!")

    while True:
        password = input("Enter a password to check its strength (or 'q' to quit): ")
        
        # Check if the user wants to exit
        if password.lower() == "q":
            print("Exiting the Password Strength Checker. Goodbye!")
            break
       
        if password == "":
            print("Password cannot be empty. Please enter a valid password.")
            continue
    
        strength = password_strength(password)

        print(f"Your Password Strength Score is: {strength} (1 to lower and 5 to higher)")
        input("\nPress any key to continue...")
        os.system("cls" if os.name == "nt" else "clear")
        
            

def word_in_file(word, filename, case_sensitive=False):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                file_word = line.strip()
                if case_sensitive:
                    if word == file_word:
                        return True
                else:
                    if word.lower() == file_word.lower():
                        return True
            return False  # Palavra não encontrada no arquivo
    except FileNotFoundError:
        print(f"Warning: File {filename} not found.")
        return False
        

def word_has_character(word, character_list):
    for letra in word :
        if letra in character_list:
            return True
    return False

def word_complexity(word):
    complexity = 0
    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1
    return complexity
    

def password_strength(password, min_length=10, strong_length=16):

    if word_in_file(password, "wordlist.txt", case_sensitive=False) == True:
        print("Password is a dictionary word and is not secure.")
        return 0
    
    if word_in_file(password, "toppasswords.txt", case_sensitive=True) == True:
        print("Password is a commonly used password and is not secure.")
        return 0
    
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1
    
    if len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5 
    
    complexity = word_complexity(password)  
    strength = 1 + complexity
    return strength

if __name__ == "__main__":
    main()
"""
Gustavo Enhacement
- Using print(current_datetime.ctime()) instead of strftime to print the current date and time.
- I create a new function request_items to handle the reading of the request file and processing the items. This improves code organization and readability.
- I created a new function show_date_info to encapsulate the logic for displaying the current date and calculating days until next year. This makes the main function cleaner and separates concerns.
"""

import csv
from datetime import datetime
from datetime import date

def main():
        
        products_dict = read_dictionary("products.csv", 0)
        print("Welcome to the Grock Store")
        print("Requested Items:")
        request_items("request.csv", products_dict)  

def read_dictionary(filename, key_column_index):
    dictionary = {}
    try:
        with open(filename, "rt", encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)

            for line in reader:
                id_product = line[key_column_index]
                dictionary[id_product] = line
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to read the file '{filename}'.")
    except IndexError:
        print(f"Error: The key column index '{key_column_index}' is out of range for the file '{filename}'.")
    return dictionary

def request_items(filename, products_dict):
    total_items = 0
    subtotal = 0.0
    try:
        with open(filename, "rt", encoding="utf-8") as request_file:
            reader = csv.reader(request_file)
            next(reader)  
            for line in reader:
                    product_id = line[0] # Product ID is in the first column example: w112
                    quantity = int(line[1]) # Quantity is in the second column example: 2
                    product_info = products_dict[product_id] # product_info is a new list received from products_dict example: ['w112', 'wheat bread', '2.55']
                    product_name = product_info[1] #
                    product_price = float(product_info[2])
                    print(f"{product_name}: {quantity} @ ${product_price:.2f}")
                    total_items += quantity
                    subtotal += product_price * quantity
        print(f"Total number of items: {total_items}")
        print(f"Subtotal: ${subtotal:.2f}")
        sales_tax = subtotal * 0.06
        print(f"Sales Tax: ${sales_tax:.2f}")
        total = subtotal + sales_tax
        print(f"Total: ${total:.2f}")
        print("Thank you for shopping at the Grock Store!")
        show_date_info()
        
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to read the file '{filename}'.")
    except KeyError as key_err:
        print(f"Error: Product ID {key_err} not found in product catalog.")

def show_date_info():
        current_datetime = datetime.now()
        print(current_datetime.ctime())
        # print(current_datetime.strftime("%a %b %d %H:%M:%S %Y"))
        current_date = date(current_datetime.year, current_datetime.month, current_datetime.day)
        year = current_date.year + 1
        goal_date = date(year, 1, 1)
        diference = goal_date - current_datetime.date()
        days_left = diference.days

        print(f"Days until next year: {days_left} days")

if __name__ == "__main__":
    main()


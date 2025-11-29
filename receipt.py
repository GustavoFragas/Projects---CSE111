import csv
import os

"""
Background
Your uncle has a grocery store, he has just started to use an online service that enables his customers to order groceries online. After a customer completes an order, the online service sends a CSV file that contains the customer’s requests to the grocery store. Your uncle has asked you to write a program that reads the CSV file and prints to the terminal window a receipt that lists the purchased items and shows the subtotal, the sales tax amount, and the total.

User Requirements
The program must read two csv files, the customer's order and a product catalog. Each item in the customer's order will be looked up in the product catalog to get get the current price. An order will be displayed in the terminal that shows the customer's order details. Use the following details to create the program.

Read the products inventory from the file products.csv.
Read the customer's order from the file request.csv
For each item in the order, look up the product in the catalog. Use the catalog information to calculate and display the order.
Display the order receipt.
Print a store name (you choose the name) at the top of the receipt.
Print the list of ordered items. Include the item name, quantity ordered and price per item.
Sum and print the number of ordered items.
Sum and print the subtotal due.
Compute and print the sales tax amount. Use 6% as the sales tax rate.
Compute and print the total amount due.
Print a thank you message.
Get the current date and time from your computer’s operating system and print the current date and time.
Include a try block and except blocks to handle FileNotFoundError, PermissionError, and KeyError.
Design
The bulk of the work for this program is performed in the main function. Make sure you include error handling as described in the user requirements.

Function Specifications
Function Name	Parameters
Return Type	Description
read_dictionary	Parameters
filename,
key_column_index
Return Tpe
Dictionary	This function reads the product data from the csv file passed to the function in the filename parameter. The dictionary key is contained in the csv data column indicated by the key_column_index parameter, the value of each dictionary item is the list derived from the values in the row of the csv file. Function returns a dictionary of products.
main		Reads the receipt.csv file, processes the file and displays the receipt according to the user requirements.
"""

def main():
    try:
        products_dict = read_dictionary("products.csv", 0)
        
        print("All Products")
        print(products_dict)
        print("Requested Items:")
        with open("request.csv", "rt", encoding="utf-8") as request_file:
            reader = csv.reader(request_file)
            next(reader)  
            for line in reader:
                product_id = line[0] # Product ID is in the first column example: w112
                quantity = int(line[1]) # Quantity is in the second column example: 2
                product_info = products_dict[product_id] # product_info is a new list received from products_dict example: ['w112', 'wheat bread', '2.55']
                product_name = product_info[1] #
                product_price = float(product_info[2])
                print(f"{product_name}: {quantity} @ ${product_price:.2f}")
    except KeyError as key_err:
        print(f"Error: Product ID {key_err} not found in product catalog.")
    

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

if __name__ == "__main__":
    main()


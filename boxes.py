"""
Problem Statement:

In our modern world economy, many items are manufactured in large factories, then packed in boxes and shipped to distribution centers and retail stores. A common question for employees who pack items is “How many boxes do we need?”

Assignment:

A manufacturing company needs a program that will help its employees pack manufactured items into boxes for shipping. Write a Python program named boxes.py that asks the user for two integers:
the number of manufactured items
the number of items that the user will pack per box
Your program must compute and print the number of boxes necessary to hold the items. This must be a whole number. Note that the last box may be packed with fewer items than the other boxes.
"""

import math

def calculate_boxes_needed(total_items, items_per_box):
    """
    Calculate the number of boxes needed to pack the items.

    Parameters:
    total_items (int): The total number of manufactured items.
    items_per_box (int): The number of items that can be packed in each box.

    Returns:
    int: The number of boxes needed.
    """
    return math.ceil(total_items / items_per_box)

def main():
    total_items = int(input("Enter the number of manufactured items: "))
    items_per_box = int(input("Enter the number of items per box: "))
    
    boxes_needed = calculate_boxes_needed(total_items, items_per_box)
    
    print(f"Number of boxes needed: {boxes_needed}")

if __name__ == "__main__":
    main()
    #
    # --- Explicação do código acima, sem usar 'def' ---
    #
    # 1. O programa pede ao usuário dois números inteiros:
    #    - total_items: quantidade de itens fabricados
    #    - items_per_box: quantidade de itens por caixa
    # 2. Para calcular o número de caixas necessárias, faz a divisão total_items / items_per_box.
    # 3. Usa math.ceil() para arredondar o resultado para cima, garantindo que todos os itens sejam embalados (mesmo que a última caixa não fique cheia).
    # 4. Mostra o resultado na tela.
    #
    # Exemplo sem função:
    # import math
    # total_items = int(input("Enter the number of manufactured items: "))
    # items_per_box = int(input("Enter the number of items per box: "))
    # boxes_needed = math.ceil(total_items / items_per_box)
    # print(f"Number of boxes needed: {boxes_needed}")
    #
    # Observação: 'calculate_boxes_needed' é uma função, sim. Em Python, 'function' é o termo correto para esse bloco de código reutilizável.

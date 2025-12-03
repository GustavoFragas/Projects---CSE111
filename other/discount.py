from datetime import datetime

DISCOUNT_RATE = 0.1  # 10% discount
TAX_RATE = .06      # 7% tax
today = datetime.now()
dow = today.weekday()  # Monday is 0 and Sunday is 6

while quantity != 0:
    quantity = int(input("Enter the quantity of items (0 to end): "))
    if quantity != 0:
        price = float(input("Enter the price of the item: $"))
        subtotal += quantity * price

subtotal = float(input("Enter the subtotal: $"))
print(f"Subtotal: ${subtotal:.2f}")

discount = 0.0
if dow in [2, 3]:  # Check if today is Wednesday or Thursday
    if subtotal >= 50:
        print(f"Discount amount: ${discount:.2f}")
        discount = subtotal * DISCOUNT_RATE
        print(f"Discount amount: ${discount:.2f}")
    else:
        short = 50 - subtotal
        print(f"Spend ${short:.2f} more to qualify for a discount.")
        
subtotal -= discount
tax = subtotal * TAX_RATE
total = subtotal + tax

print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
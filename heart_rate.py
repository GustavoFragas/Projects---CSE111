"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

def calculate_heart_rate_range(age):
    """
    Calculate the target heart rate range for strengthening the heart.

    Parameters:
    age (int): The age of the person.

    Returns:
    tuple: A tuple containing the lower and upper bounds of the target heart rate range.
    """
    max_heart_rate = 220 - age
    lower_bound = round(max_heart_rate * 0.65)
    upper_bound = round(max_heart_rate * 0.85)
    return (lower_bound, upper_bound)

def main():
    age = int(input("Please enter your age: "))
    lower, upper = calculate_heart_rate_range(age)
    print("When you exercise to strengthen your heart, you should")
    print(f"keep your heart rate between {lower} and {upper} beats per minute.")

if __name__ == "__main__":
    main()

x = 5
y = 10
z = 15

print(x, y, z, sep=' | ', end='\n', file=None, flush=False)


import random
import math
def number_program():
    try:
        numbers = set()
        print("---Enter 10 numbers---")
        for i in range(10):
            num = int(input("Enter number : "))
            numbers.add(num)
        print("\nUnique numbers (Set):", numbers)
        numbers_tuple = tuple(numbers)
        print("Tuple:", numbers_tuple)
        if len(numbers_tuple) >= 3:
            random_numbers = random.sample(numbers_tuple, 3)
            print("3 Random numbers:", random_numbers)
        else:
            print("Not enough unique numbers to pick 3 random values.")
        total = sum(numbers_tuple)
        sqrt_value = math.sqrt(total)
        print("Sum of tuple elements:", total)
        print("Square root of sum:", sqrt_value)
    except ValueError:
        print("Invalid input! Please enter numeric values.")
    except Exception as e:
        print("Error occurred:", e)
number_program()
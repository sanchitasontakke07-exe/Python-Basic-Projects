import math
import random
from datetime import datetime
results = {}
def calculator():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        choice = int(input("Choose operation: "))
        if choice == 1:
            result = a + b
        elif choice == 2:
            result = a - b
        elif choice == 3:
            result = a * b
        elif choice == 4:
            result = a / b
        else:
            print("Invalid choice")
            return
        print("Result:", result)
        results[str(datetime.now())] = result
    except:
        print("Invalid input")
def scientific():
    try:
        num = float(input("Enter number: "))
        print("Square root:", math.sqrt(num))
        print("Square:", math.pow(num, 2))
        results[str(datetime.now())] = math.sqrt(num)
    except:
        print("Invalid input")
def random_numbers():
    try:
        nums = []
        for i in range(5):
            nums.append(random.randint(1, 100))
        print("Random Numbers:", nums)
        results[str(datetime.now())] = nums
    except:
        print("Error occurred")
def view_history():
    if results:
        print("\n--- History ---")
        for key, value in results.items():
            print(key, ":", value)
    else:
        print("No history available")
while True:
    print("\n--- Smart Calculator & Data Manager ---")
    print("1. Basic Arithmetic")
    print("2. Scientific Calculations")
    print("3. Generate Random Numbers")
    print("4. View History")
    print("5. Exit")
    try:
        choice = int(input("Enter choice: "))
        if choice == 1:
            calculator()
        elif choice == 2:
            scientific()
        elif choice == 3:
            random_numbers()
        elif choice == 4:
            view_history()
        elif choice == 5:
            print("Program exited")
            break
        else:
            print("Invalid choice")
    except:
        print("enter valid option")
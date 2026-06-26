def square_program():
    try:
        square = lambda x: x * x
        squares = []
        for i in range(1, 21):
            squares.append(square(i))
        print("Squares of numbers 1 to 20:")
        print(squares)
        even_squares = []
        for num in squares:
            if num % 2 == 0:
                even_squares.append(num)
        print("\nEven squares:")
        print(even_squares)
    except Exception as e:
        print("Error:", e)
square_program()
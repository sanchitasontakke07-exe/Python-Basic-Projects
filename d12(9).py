# Strings + Sets + Exception Handling + Modules

import math

def unique_words_program():
    try:
        sentence = input("Enter a sentence: ")

        # Convert sentence into words
        words = sentence.split()

        # Store unique words in set
        unique_words = set(words)

        # Sort and display unique words
        sorted_words = sorted(unique_words)

        print("\nUnique words in sorted order:")
        for word in sorted_words:
            print(word)

        # Count unique words and calculate square
        total_words = len(unique_words)

        result = math.pow(total_words, 2)

        print("\nTotal unique words:", total_words)
        print("Square of unique words count:", result)

    except:
        print("An error occurred")


# Function call
unique_words_program()
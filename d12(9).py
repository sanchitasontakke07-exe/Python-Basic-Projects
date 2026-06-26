import math
def unique_words_program():
    try:
        sentence = input("Enter a sentence: ")
        words = sentence.split()
        unique_words = set(words)
        sorted_words = sorted(unique_words)
        print("\nUnique words in sorted order:")
        for word in sorted_words:
            print(word)
        total_words = len(unique_words)
        result = math.pow(total_words, 2)
        print("\nTotal unique words:", total_words)
        print("Square of unique words count:", result)
    except:
        print("An error occurred")
unique_words_program()
def count_words(sentence):

    #Count the number of words in a sentence.
    # Check for empty input
    if not sentence.strip():
        return 0  # Return 0 for empty input

    # Split the sentence into words based on spaces
    words = sentence.split()
    # Count the number of words
    return len(words)


def main():

    #to execute the word count program
    print("Welcome to the Word Counter program!")

    while True:
        user_input = input("Enter a sentence or paragraph (or 'exit' to quit): ")

        if user_input.lower() == 'exit':
            print("Thank you for using the Word Counter. Goodbye!")
            break

        # Call the function
        word_count = count_words(user_input)
        print(f"Word count: {word_count}\n")


if __name__ == "__main__":
    main()


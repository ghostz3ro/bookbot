from stats import get_num_words, count_of_characters, sort_on
import sys

# Reading the text of the book as a single string from a filepath input and returning it as one string.
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents


# Setting the filepath and calling functions to get the text of the book and the number of words,
# filepath = "books/frankenstein.txt"
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    word_count = get_num_words(book_text)

    # Calling the sort function and the character counting function in the same line
    character_appearances = sort_on(count_of_characters(book_text))
    #sorted_dict = sort_on(character_appearances)

    # Starting printing in accordance with the required report layout 
    print(f"Analysing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in character_appearances: 
        if char.isalpha() is True:
            print(f"{char}: {character_appearances[char]}")

    print("============= END ===============")
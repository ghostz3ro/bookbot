# Function to get number of words of an string input
def get_num_words(text):
    
    word_list = []
    word_list = text.split()
    number_of_words = 0
    
    for i in range(0,len(word_list)):
        number_of_words += 1

    return number_of_words


# Counting the character occurrences for each character
def count_of_characters(input_string):

    # Setting the string to all lowercase, creating a blank dictionary and creating a list of all the characters 
    lowercase_string = input_string.lower() 
    character_count = {}
    character_list = list(lowercase_string)
    
    # Changing the list of characters to a set to remove duplicates
    character_set = set(character_list)

    # Counting the character occurences
    for character in character_set:
        character_count[character] = character_list.count(character)

    return character_count

def sort_on(items):
    # Creating a list of dictionaries with each character:numberofoccurrences item
    sort_list= list(items.items())

    # Sorting algorythm using as sorting key the second item from each touple, example in {a: 15000} -> "a": 15000 item[0] is "a" and item[1] is "15000" 
    # reverse=True means big to small or z to a etc
    sort_list.sort(reverse=True, key=lambda item:item[1])
    # Making the list back to a dictionary
    sorted_dictionary = dict(sort_list)
    
    return sorted_dictionary
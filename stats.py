def count_words(file: str) -> int:
    ### Returns the word count for a given file

    words = file.split()
    word_count = len(words)

    return word_count

def count_characters(file: str) -> dict:
    ### Iterates through a string and counts the frequency of each unique 
    ### character

    character_count = {}

    file = file.lower()
   
    for c in range(len(file)):
        char = file[c]

        if char not in character_count:
            character_count[char] = 1
        else: 
            character_count[char] += 1

    return character_count

def sort_characters(dictionary: dict) -> list:
    ### Creates a list filled with one-item dictionaries representing each
    ### character present sorted by frequency

    characters = []

    for key in dictionary:

        entry = dict(char = key, num = dictionary[key])
        characters.append(entry)

    characters.sort(reverse = True, key = sort_on)

    return characters

def sort_on(dictionary):
    ### Helper function for sorting lists by dictionary key-value pairs ###

    return dictionary["num"] # {char, num}

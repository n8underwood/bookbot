import stats
import sys

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        
        sys.exit(1)

    file_contents = get_book_text(sys.argv[1])
    
    word_count = stats.count_words(file_contents)
    characters = stats.count_characters(file_contents)
    sorted_characters = stats.sort_characters(characters)

    print_report(word_count, sorted_characters)

def get_book_text(file: str) -> str:
    
    with open(file) as f:
        file_contents = f.read()

    return file_contents

def print_report(word_count: int, characters: list) -> None:
    
    # Header
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")

    # Words
    print(f"Found {word_count} total words")

    # Characters
    print("--------- Character Count -------")
    for i in range(len(characters)):
        pair = characters[i] # Fetch character data from dictionary
        char = pair["char"]
        count = pair["num"]

        if char.isalpha(): # Only print letters
            print(f"{char}: {count}")


if __name__ == "__main__":
    main()

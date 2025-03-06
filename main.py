from stats import count_words
from stats import count_letters
from stats import alpha_only
import sys


def get_book_text(filepath):
    file_contents= None
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_location = sys.argv[1]
    book = get_book_text(book_location)
    word_count = count_words(book)
    

    
    letter_count = count_letters(book)
    alpha_dict =alpha_only(letter_count)
    sorted_dit = dict(sorted(alpha_dict.items(), key=lambda item: item[1] , reverse=True))
    

    print("=========== BOOKBOT ============")
    print(f"Analyzing book found at {book_location}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for a in sorted_dit:
        print(f"{a}: {sorted_dit[a]}")
    print("============= END ===============")


main()
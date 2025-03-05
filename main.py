from stats import count_words
from stats import count_letters

def get_book_text(filepath):
    file_contents= None
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents


def main():
    book_location = "books/frankenstein.txt"
    book = get_book_text(book_location)
    word_count = count_words(book)
    

    print(f"{word_count} words found in the document")
    letter_count = count_letters(book)
    
    sorted_dit = dict(sorted(letter_count.items(), key=lambda item: item[1] , reverse=True))
    print(sorted_dit)



main()
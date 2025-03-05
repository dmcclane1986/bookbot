from stats import count_words

def get_book_text(filepath):
    file_contents= None
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents


def main():
    book = get_book_text("books/frankenstein.txt")
    word_count = count_words(book)
    print(f"{word_count} words found in the document")



main()
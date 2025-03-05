def get_book_text(filepath):
    file_contents= None
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents

def count_words(book):
    count = 0
    words = book.split()
   
    for word in words:
        count += 1
    return count


def main():
    book = get_book_text("books/frankenstein.txt")
    word_count = count_words(book)
    print(f"{word_count} words found in the document")



main()
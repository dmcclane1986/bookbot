def count_words(book):
    count = 0
    words = book.split()
   
    for word in words:
        count += 1
    return count
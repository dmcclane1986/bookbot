def count_words(book):
    count = 0
    words = book.split()
   
    for word in words:
        count += 1
    return count

def count_letters(book):
    letters_dit = {}
    words = book.split()
    for word in words:
        letters = word.lower()
        for l in letters:
            if l in letters_dit:
                letters_dit[l]+=1
            else: 
                letters_dit[l] =1
    return letters_dit

def alpha_only(dict):
    alpha_dict = {}
    for a in dict:
        if a.isalpha():
            alpha_dict[a]=dict[a] 
    return alpha_dict
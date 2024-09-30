def main():
    book = pick_book()
    book_contents = open_book(book)
    book_chars = chars_count(book_contents)

    print(f"\n--- Begin report of {book} ---\n")
    print(f"{book_wordcount(book_contents)} words found in the text.\n")

    for char, num in book_chars.items():
        print(f"The char {char} was found {num} times.")
    print("\n--- End report ---\n")


def pick_book():
    return "books/frankenstein.txt"

#locates and opens book file    
def open_book(book):   
    with open(book) as f:
        file_contents = f.read()
    return file_contents

#returns number of words in book
def book_wordcount(book):
    return len(book.split())

#counts chars, filters to letters only, sorts by greatest
def chars_count(book):
    chars = {}
    sorted_chars = {}

    #count each char occurrence
    for c in book:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
            
    #remove special chars
    for c in chars:
        if c.isalpha():
            sorted_chars[c] = chars[c]
    
    #sort from largest to smallest
    sorted_chars = dict(sorted(sorted_chars.items(), key=lambda item: item[1], reverse=True))
    return sorted_chars


main()
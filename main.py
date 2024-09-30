def main():
    book = pick_book()
    book_contents = open_book(book)
    book_chars = chars_count(book_contents)

    print(f"--- Begin report of {book} ---")
    print(f"{book_wordcount(book_contents)} words found in the text.\n\n")

    for char, num in book_chars.items():
        print(f"The char {char} was found {num} times.")


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

def chars_count(book):
    chars = {}
    for c in book:
        if c != " ":
            lowered = c.lower()
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    sorted_chars = dict(sorted(chars.items(), key=lambda item: item[1], reverse=True))
    return sorted_chars

main()
def main():
    book_path = "books/frankenstein.txt"
    retrieve_book(book_path)
    count_words(book_path)
    count_chars(book_path)

def retrieve_book(book):
    with open(book) as f:
     return f.read()

def count_words(book):
    words = book.split()
    print(f"There were {len(words)} words in this book.")

def count_chars(book):
    book_lower_case = book.lower()
    chars = {"a", "b", "c", }
    count_dict = {}
    for char in chars:
        count = 0
        for book_char in book:
            if char == book_char:
                count += 1
        count_dict.update({char:count})
        print(f"The {char} character was found {count} times.")
    # WIP, sort chars highest to lowest


main()

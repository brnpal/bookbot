def main():
    book_path = "books/frankenstein.txt"
    count_words(book_path)
    count_chars(book_path)
    with open(book_path) as f:
        return f.read()
    

def count_words(text):
    words = text.split()
    print(f"There were {len(words)} words in this book.")

def count_chars(book):
    book_lower_case = book.lower()
    chars = {"a", "b", "c"}
    count_dict = {}
    for char in chars:
        count = 0
        for book_char in book:
            if char == book_char:
                count += 1
        count_dict.update({char:count})
    return count_dict

main()

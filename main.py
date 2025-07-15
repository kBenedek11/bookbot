from stats import count_words
from stats import count_character

def get_book_text(filepath):
    with open(filepath) as f:
        content_as_string = f.read()
    return content_as_string

def main():
    book = get_book_text("books/frankenstein.txt")
    num_of_words = count_words(book)
    character_count = count_character(book)
    print(f"{num_of_words} words found in the document")
    print(character_count)

main()
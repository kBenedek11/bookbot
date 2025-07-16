from stats import count_words
from stats import count_character
from stats import sort_list

def get_book_text(filepath):
    with open(filepath) as f:
        content_as_string = f.read()
    return content_as_string

def main():
    book = get_book_text("books/frankenstein.txt")
    num_of_words = count_words(book)
    character_count = count_character(book)
    sorted_list_of_charactercount = sort_list(character_count)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    for element in sorted_list_of_charactercount:
        if element["char"].isalpha():
            print(f"{element["char"]}: {element["num"]}")
    print("============= END ===============")

main()
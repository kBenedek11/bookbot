def count_words(text):
    word_list = text.split()
    num_of_words = len(word_list)
    return num_of_words

def count_character(text):
    character_dictionary = {}
    lowercase_text = text.lower()
    character_list = list(lowercase_text)
    for char in character_list:
        if char in character_dictionary:
            character_dictionary[char] += 1
        else:
            character_dictionary[char] = 1
    return character_dictionary
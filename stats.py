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

def sort_on(items):
    return items["num"]

def sort_list(dictionary):
    dictionary_list = []
    for  key_ in dictionary:
        dictionary_list.append({"char" : key_, "num" : dictionary[key_]})
    dictionary_list.sort(reverse=True, key=sort_on)
    return  dictionary_list
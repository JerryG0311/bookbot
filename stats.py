def count_words(text):
    return len(text.split())

def count_characters(text):
    count = {}
    for chars in text:
        char = chars.lower()
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count 

def sort_on(dict):
    return dict["num"]

def sort_list(count):
    all_character_data = []
    for character, number in count.items():
        single_char_dict = {}
        single_char_dict["char"] = character
        single_char_dict["num"] = number
        all_character_data.append(single_char_dict)
    all_character_data.sort(reverse=True, key=sort_on) 
    return all_character_data


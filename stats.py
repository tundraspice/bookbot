def get_word_count(text):
    word_count = len(text.split())
    return word_count


def get_num_of_chars(text):
    chars = {}
    for char in text.lower():
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    return chars

def sort_on(d):
    return d["num"]


def get_sorted_num_of_chars(chars_dict):
    sorted_list = []
    for char in chars_dict:
        sorted_list.append({"char": char, "num": chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

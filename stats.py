

def get_word_count(text):
    return len(text.split())

def get_chars_dict(text):
    chars_dict = {}
    for c in text:
        if c not in chars_dict:
            chars_dict[c] = 1
        else:
            chars_dict[c] += 1
    return chars_dict

def sort_on(d):
    return d["num"]

def get_sorted_chars_dict(chars_dict):
    sorted = []
    for char in chars_dict:
        sorted.append({"char": char, "num": chars_dict[char]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted
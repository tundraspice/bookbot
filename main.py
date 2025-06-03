import sys
from stats import get_word_count, get_chars_dict, get_sorted_chars_dict

def main():
    if len(sys.argv) == 2:
        path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
   
    text = get_text(path)
    word_count = get_word_count(text)
    chars_dict = get_chars_dict(text)
    sorted_chars_list = get_sorted_chars_dict(chars_dict)
    print_result(path, word_count, sorted_chars_list)

def get_text(path):
    with open(path) as f:
        return f.read() 

def print_result(path, word_count, sorted_chars_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_chars_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")


main()
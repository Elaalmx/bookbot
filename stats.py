def count_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def count_characters(text):
    counts = {}
    words = text.lower()
    for char in words:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def sort_on(items):
    return items["num"]

def sort_character_counts(char_dict):
    # Convert to list of {"char": ..., "num": ...}
    char_list = [{"char": c, "num": n} for c, n in char_dict.items()]
    char_list.sort(key=sort_on, reverse=True)
    return char_list

def print_character_report(char_list):
    for item in char_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

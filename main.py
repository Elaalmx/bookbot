import sys
from stats import count_words, count_characters, sort_character_counts, print_character_report

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    count_all_words = count_characters(book_text)
    sorted_char_counts = sort_character_counts(count_all_words)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    print_character_report(sorted_char_counts)
    print("============= END ===============")

main()

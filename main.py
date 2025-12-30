import sys
from stats import get_count_words, get_count_char, print_report


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
    

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1]
    file_book = get_book_text(path_to_book)
    num_words = get_count_words(file_book)
    num_chars = get_count_char(file_book)

    print_report(path_to_book, num_words, num_chars)

main()
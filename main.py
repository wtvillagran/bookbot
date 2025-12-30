from stats import get_count_words, get_count_char


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents



def main():
    path_to_book = "/Users/williamvillagran/Desktop/projects/Bookbot/books/frankenstein.txt"
    file_book = get_book_text(path_to_book)

    num_words = get_count_words(file_book)

    print(f"Found {num_words} total words")

    num_chars = get_count_char(file_book)
    
    print(num_chars)

main()
def get_count_words(file):
    count = file.split()
    return len(count)

def get_count_char(file):

    count_char = {}
    for character in file:
        if character.isalpha():
            char_lower = character.lower()
            if char_lower not in count_char:
                count_char[char_lower] = 1
            else:
                count_char[char_lower] += 1
    return count_char

print_dict = lambda d: [print(f"{item[0]}: {item[1]}") for item in sorted(d.items(), key=lambda x: x[1], reverse=True) if ord(item[0]) < 128]

def print_report(file_path, word_count, char_count):
    print("============ BOOKBOT ============\n" \
    f"Analyzing book found at {file_path}\n" \
    "----------- Word Count ----------\n" \
    f"Found {word_count} total words\n" \
    f"--------- Character Count -------\n")
    print_dict(char_count)
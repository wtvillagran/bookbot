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
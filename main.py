def main():
    book_path = "./books/frankenstein.txt"
    book_text = get_book_text(book_path)
    book_character_dict = get_character_counts(book_text)
    print(book_character_dict)

def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_counts(text):
    character_counts = {}
    for char in text:
        lowercase = char.lower()
        if lowercase in character_counts:
            character_counts[lowercase] += 1
        else:
            character_counts[lowercase] = 1

    return character_counts

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()

        return file_contents

main()

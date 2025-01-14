import string

def main():
    book_name = "frankenstein.txt"
    book_path = f"books/{book_name}"
    book_text = get_book_text(book_path)
    book_character_dict = get_character_counts(book_text)
    print_character_report(book_character_dict, book_path, get_word_count(book_text))

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

def print_character_report(character_dict, book_path, word_count):
    letters = list(string.ascii_lowercase)
    sorted_characters = sorted(character_dict.items(), key=lambda x: x[1], reverse=True)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the book.")
    print("")
    for item in sorted_characters:
        char, count = item
        if char not in letters:
            continue
        print(f"The '{char}' character was found {count} times.")

    print("--- End report ---")


main()

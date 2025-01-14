def main():
    book_path = "./books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    print(f"There are {word_count} words in the book.")

def get_word_count(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()

        return file_contents

main()

# Python executable main file

from stats import book_word_count, book_word_occurences

def get_book_text(path_to_file: str) -> str:

    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():

    path_to_book = "./books/frankenstein.txt"
    book_text = get_book_text(path_to_book)
    word_count = book_word_count(book_text)
    char_occurences: dict[str, int] = book_word_occurences(book_text)

    print(char_occurences)
    print(f"Found {word_count} total words")

main()


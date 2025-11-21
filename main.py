# Python executable main file

def get_book_text(path_to_file: str) -> str:

    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def book_word_count(text_in_file: str) -> int:
    return len(text_in_file.split(" "))

def main():

    path_to_book = "./books/frankenstein.txt"
    book_text = get_book_text(path_to_book)
    word_count = book_word_count(book_text)

    print(get_book_text(path_to_book))
    print(f"Word count: {word_count}")

main()


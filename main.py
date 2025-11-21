# Python executable main file

from stats import book_word_count, book_char_occurences, sort_char_occurences

def get_book_text(path_to_file: str) -> str:

    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():

    path_to_book = "books/frankenstein.txt"
    book_text = get_book_text(path_to_book)
    word_count = book_word_count(book_text)
    char_occurences: dict[str, int] = book_char_occurences(book_text)
    sorted_occurences: list[dict[str, str | int]] = sort_char_occurences(char_occurences)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_occurences:
        print(f"{char_dict["char"]}: {char_dict["num"]}")
    print("============= END ===============")

main()


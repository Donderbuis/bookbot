# Stats file

def book_word_count(book_text: str) -> int:
    return len(book_text.split())

def book_char_occurences(book_text: str) -> dict[str, int]:
    charset: set[str] = set()
    chardict: dict[str, int] = {}

    for char in book_text:
        char = char.lower()
        if char in charset:
            chardict[char] += 1
        else:
            charset.add(char)
            chardict[char] = 1

    return chardict

def sort_on(chars: dict[str, str | int]):
    return chars["num"]

def sort_char_occurences(char_occurences: dict[str, int]) -> list[dict[str, str | int]]:
    ordered_list: list[dict[str, str | int]] = []

    for char in char_occurences:
        if not char.isalpha():
            continue
        refactor_dict: dict[str, str | int] = {"char": char, "num": 0}
        refactor_dict["num"] = char_occurences[char]
        ordered_list.append(refactor_dict)

    ordered_list.sort(reverse=True, key=sort_on)
    return ordered_list


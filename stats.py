# Stats file

def book_word_count(book_text: str) -> int:
    return len(book_text.split())

def book_word_occurences(book_text: str) -> dict[str, int]:
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


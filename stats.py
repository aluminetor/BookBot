def get_num_words(text: str) -> int:
    return len(text.split())


def get_chars_dict(text: str) -> dict[str, int]:
    chars = {}
    for char in text.lower():
        chars[char] = chars.get(char, 0) + 1
    return chars


def sort_on(item: tuple[str, int]) -> int:
    return item[1]


def chars_dict_to_sorted_list(chars_dict: dict[str, int]) -> list[tuple[str, int]]:
    sorted_list = []
    for char, count in chars_dict.items():
        sorted_list.append((char, count))
    return sorted(sorted_list, reverse=True, key=sort_on)
from stats import get_num_words, get_chars_dict, chars_dict_to_sorted_list
import sys

def get_book_text(path_to_file: str) -> str:
    with open(path_to_file) as f:
        return f.read()

def print_report(path_to_file: str, num_words: int, sorted_chars: list[tuple[str, int]]) -> None:
    print("=========== BOOKBOT ===========")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char, count in sorted_chars:
        if char.isalpha():
            print(f"{char}: {count}")
    print("============ END ================")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    text = get_book_text(path_to_file)

    chars_dict = get_chars_dict(text)
    sorted_chars = chars_dict_to_sorted_list(chars_dict)
    
    num_words = get_num_words(text)
    print_report(path_to_file, num_words, sorted_chars)


if __name__ == "__main__":
    main()
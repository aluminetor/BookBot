from stats import get_count_words,get_num_character


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    
def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    words = get_count_words(path_to_file) 
    num_character = get_num_character(path_to_file)

    print(text,words,num_character)



main()
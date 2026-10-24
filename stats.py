def get_count_words(path_to_file):
    with open(path_to_file) as f:
        words = f.read().split()

    return f"Found {len(words)} total words"

def get_num_character(path_to_file):
    with open(path_to_file) as f:
            words = f.read().lower()
    
    boot = {}

    for caracter in words:
        boot[caracter] = boot.get(caracter, 0) + 1

    return boot

def sort_on(sort: tuple[str,int]) -> int:
    return sort[1]

def chars_dict_to_sorted_list(lista: dict[str,int]) -> list[tuple[str, int]]:
    lista_vacia = []

    for caracter in lista:
         
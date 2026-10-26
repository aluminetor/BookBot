# bookbot

[![Boot.dev Build a BookBot in Python certificate](https://qvault-webapp-dynamic-assets.storage.googleapis.com/certificates/b14641ac-a46d-4e4f-9044-38e4e7f6cab8.jpeg?v=1792976008)](https://www.boot.dev/certificates/b14641ac-a46d-4e4f-9044-38e4e7f6cab8)

BookBot is my first [Boot.dev](https://www.boot.dev) project!

BookBot lee un archivo de texto y genera un pequeño reporte con el conteo total
de palabras y la frecuencia de cada carácter alfabético.

## Requisitos

- Python 3.9 o superior (el código usa anotaciones de tipo genéricas como
  `dict[str, int]` y `list[tuple[str, int]]`).

## Uso

El libro a analizar se define en `main.py`:

```python
path_to_file = "books/frankenstein.txt"
```

Para ejecutar el reporte, desde la raíz del proyecto:

```bash
python3 main.py
```

### Libros incluidos

| Libro                 | Ruta                            |
| --------------------- | ------------------------------- |
| Frankenstein          | `books/frankenstein.txt`        |
| Moby Dick             | `books/mobydick.txt`            |
| Pride and Prejudice   | `books/prideandprejudice.txt`   |

Para analizar otro libro, cambia el valor de `path_to_file` por cualquiera de
las rutas de la tabla.

## Salida esperada

```text
=========== BOOKBOT ===========
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 78150 total words
--------- Character Count -------
e: 46043
t: 30365
a: 26743
...
============ END ================
```

Solo se listan los caracteres alfabéticos, ordenados de mayor a menor frecuencia.

## Estructura del proyecto

```text
bookbot/
├── main.py     # Punto de entrada: lectura del libro e impresión del reporte
├── stats.py    # Lógica de conteo de palabras y caracteres
└── books/      # Archivos de texto de los libros
```

### `stats.py`

- `get_num_words(text)` — devuelve el número total de palabras.
- `get_chars_dict(text)` — devuelve un diccionario con la frecuencia de cada
  carácter (en minúsculas).
- `chars_dict_to_sorted_list(chars_dict)` — convierte ese diccionario en una
  lista de tuplas `(carácter, conteo)` ordenada de mayor a menor.

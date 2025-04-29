from stats import *
import sys

def main(path):
    chars = dict_to_list(count_chars(get_book_text(path)))
    chars.sort(reverse = True, key = sort_on)
    print('============ BOOKBOT ============')
    print('Analyzing book found at ' + path + "...")
    print('----------- Word Count ----------')
    print(f'Found {count_words(get_book_text(path))} total words')
    print('--------- Character Count -------')

    print_char_stats(chars)
    print('============= END ===============')

try:
    main(sys.argv[1])
except IndexError:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
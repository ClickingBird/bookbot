def get_book_text(path):
    with open(path) as text:
        content = text.read()
    return content

def count_words(text):
    counter = 0
    split_text = text.split()
    num_words = len(split_text)
    return num_words

def count_chars(text):
    char_dict = {}
    for i in text.lower():
        if i not in char_dict:
            char_dict[i] = 1
        else:
            char_dict[i] += 1
    return char_dict

def dict_to_list(dict):
    dict_list = []
    for k,v in dict.items():
        dict_list.append({'char': k, 'num': v})
    return dict_list
 
def sort_on(dict):
    return dict['num']

def print_char_stats(char_list):
    for i in char_list:
        if i['char'].isalpha() == False:
            continue
        else:
            print(f'{i['char']}: {i['num']}')

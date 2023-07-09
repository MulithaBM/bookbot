def main() :
    book_path = "books/frankenstein.txt"
    text = read_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_char_dict(text)
    sorted_char_list = sort_char_dict(char_dict)
    report(book_path, num_words, sorted_char_list)

def read_text(path) :
    with open(path) as f :
        return f.read()

def get_num_words(text) :
    return len(text.split())

def get_char_dict(text) :
    frequency = {}

    for char in text :
        lower_case = char.lower()

        if lower_case in frequency :
            frequency[lower_case] += 1
        else :
            frequency[lower_case] = 1

    return frequency

def sort_char_dict(char_dict) :
    sorted_list = []

    for char in char_dict :
        sorted_list.append([char, char_dict[char]])

    sorted_list.sort(key= lambda a: a[1], reverse=True)

    return sorted_list

def report(path, num_words, char_dict) :
    print("--- Begin report of {} ---".format(path))
    print("{} words found in the document".format(num_words))
    print()
    
    for char in char_dict :
        if char[0].isalpha() :
            print("The '{0}' character was found {1} times".format(char[0], char[1]))

    print("--- End report ---")

main()
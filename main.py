def main():
    path = "books/frankenstein.txt"
    file_contents = get_text(path)
    num_words = count_words(file_contents)
    char_dict = char_counter(file_contents)
    chars_sorted_list = chars_dict_to_sorted_list(char_dict)
    
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document")

    for key in chars_sorted_list:
        if not key["char"].isalpha():
            continue
        print(f"The '{key}' character was found {key['num']} times")

    print("--- End report ---")

def get_text(path):
    with open(path)as f:
        return f.read()

def count_words(file_contents):
    # Calculate the number of words
    words = file_contents.split()
    return len(words)

def char_counter(file_contents):
    # Counts iteration of each character
    counter = {}
    for i in file_contents:
        char = i.lower()
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
    return counter

def sort_on(d):
    return d["num"]
    
def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()


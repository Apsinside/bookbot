def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def get_word_count(text):
    return len(text.split())

def get_char_count(text):
    char_count = {}
    for string in text.split():
        for char in string:
            char = char.lower() 
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def sort_on(dict):
    return dict["num"]

def sort_char_count(char_count):
    sorted_char_counts = []
    for key in char_count:
        sorted_char_counts.append({"char" : key, "num":char_count[key] })
    sorted_char_counts.sort(reverse=True, key=sort_on)
    return sorted_char_counts

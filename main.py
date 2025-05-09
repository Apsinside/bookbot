import sys
from stats import get_book_text
from stats import get_word_count
from stats import get_char_count
from stats import sort_char_count

def main():
    if len(sys.argv) != 2  :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    book_text = get_book_text(sys.argv[1])
    print(f"Found {get_word_count(book_text)} total words")
    print("--------- Character Count -------")
    char_counts = get_char_count(book_text)
    for char_count in sort_char_count(char_counts):
        if not char_count["char"].isalpha():
            continue
        print(f"{char_count['char']}: {char_count['num']}")
    print("============= END ===============")

main()
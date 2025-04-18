import sys
from stats import count_words
from stats import count_chars
from stats import sorted_chars

def get_book_text(path : str) -> str:
    with open(path) as f:
        content = f.read()
        return content

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    count = count_chars(text)
    sorted_dicts = sorted_chars(count)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print("Found", count_words(text), "total words")
    print("--------- Character Count -------")
    for d in sorted_dicts :
        if d["char"].isalpha():
            print(f"{d["char"]}: {d["count"]}")
    print("============= END ===============")
    
main()
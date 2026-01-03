from stats import count_words, count_characters, sort_characters_dict
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents



def main():
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    char_count = count_characters(book_text)
    sorted_count = sort_characters_dict(char_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count -----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_count:
        char = item["char"]
        num = item["num"]
        if not char.isalpha():
            continue
        print(f"{char}: {num}")
    print("============= END ===============")
main()
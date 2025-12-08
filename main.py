from stats import get_characters_count, get_num_words, get_sorted_characters
import sys

def main():
    args = sys.argv

    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = args[1]

    def get_book_text(path_to_file) -> str:
        with open(path_to_file) as f:
            return f.read()

    book_text = get_book_text(book_path)
    word_count = get_num_words(book_text)
    characters = get_characters_count(book_text)
    sorted_list = get_sorted_characters(characters)

    def print_summary():
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")

        for item in sorted_list:
           if item["char"].isalpha():
               print(f"{item['char']}: {item['num']}")


        print("============= END ===============")

    return print_summary()

if __name__=="__main__":
    main()
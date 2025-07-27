from stats import get_contents, get_words, count_words
import sys

# next bikin lable biar nggk binging


def main():
    if len(sys.argv) < 2:
        input("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_name = sys.argv[1]
        book_contents = get_contents(book_name)
        book_words = get_words(book_contents)
        book_words_count = count_words(book_words)
        print("============ BOOKBOT ============")
        print(f"analying book of: {book_name}")
        print("---------- total words ----------")
        print(f"{len(book_words)} worlds")
        print("------- top worlds appear -------")
        for tword, tnum in book_words_count[:10]:
            print(f"{tword}: {tnum}")


if __name__ == "__main__":
    main()

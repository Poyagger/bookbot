from stats import get_contents, get_words, count_words


def main():
    book_name = input("txt file pliss : ")
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

from stats import get_words, count_words

def main():
    print('hilo')
    book = get_book(input('file pliss : '))
    count_words(get_words(book))

def get_book(ibook):
    with open(ibook) as target:
        return target.read()

if __name__ == '__main__':
    main()

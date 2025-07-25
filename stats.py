def get_words(i):
    words = i.split()
    print(f"{len(words)} total worlds")
    return words


def count_words(arry):
    word = {}

    for i in arry:
        lowercase_word = i.lower()
        if lowercase_word in word:
            word[lowercase_word] += 1
        else:
            word[lowercase_word] = 1

    sorted_word = sorted(word.items(), key=lambda item: item[1], reverse=True)
    print("top 10 word appear: ")

    for tword, tnum in sorted_word[:10]:
        print(f"{tword}: {tnum}")


# def count_alphabet:

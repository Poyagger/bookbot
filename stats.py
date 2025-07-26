def get_contents(ibook):
    with open(ibook) as target:
        return target.read()


def get_words(i):
    words = i.split()
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
    return sorted_word


# def count_alphabet:

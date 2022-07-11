def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

def check_if_len_five(word):
    length = len(word)
    value = False
    if len(word) == 5:
        value = True
    return value

def return_only_if_five(word):
    if check_if_len_five(word):
        return word
    else:
        pass

def reduce_list_to_only_five_letters(wordlist):
    #reduce wordset to only five letter words
    newlist = [return_only_if_five(word) for word in wordlist]
    #if five, then add to the new set
    newlist = [word for word in newlist if word]
    return newlist

#Main is really just so I can test this function library works
"""
if __name__ == '__main__':
    english_words = list(load_words())
    # demo print
    new_wordlist = reduce_list_to_only_five_letters(english_words)
    print(new_wordlist)
"""

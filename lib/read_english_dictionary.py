nonstandard_chars = ""
acceptable_chars = "qwertyuiopasdfghjklzxcvbnm"
acceptable_chars = "abcdefghijklmnopqrstuvwxyz"

def alphabetical(word):
    for 

def load_words(filename):
    with open(filename) as word_file:
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

def eliminate_nonstandard_char_words(wordlist):
    #you can make your set by removing all letters from the wordlist realquick
    newlist = [word for word in wordlist if word.isalpha()]
    newlist = [word for word in wordlist if word]
    return wordlist

def eliminate_allcaps_words(wordlist):
    newlist = [word for word in wordlist if not word.isupper()]
    newlist = [word for word in newlist if word]
    return newlist
    
def lowercase_all_words(wordlist):
    newlist = eliminate_allcaps_words(wordlist)
    newlist = [word.lower() for word in wordlist]
    return newlist


#Main is really just so I can test this function library works

if __name__ == '__main__':
    english_words = list(load_words( "~/wordle-helper/words_alpha.txt"))
    # demo print
    new_wordlist = reduce_list_to_only_five_letters(english_words)
    new_wordlist = eliminate_nonstandard_char_words
    new_wordlist = lowercase_all_words
    print(new_wordlist)


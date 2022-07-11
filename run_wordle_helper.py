#main.py
import download_new_wordlist
import read_english_dictionary


if __name__ == '__main__':

    #
    english_words = list(load_words())
    # demo print
    new_wordlist = reduce_list_to_only_five_letters(english_words)
    print(new_wordlist)

#main.py
import lib.download_new_wordlist as download
import lib.read_english_dictionary as reader


if __name__ == '__main__':

    #get list and reduce to five letter words then print them
    filename = download.download_and_overwrite_wordlist()
    english_words = list(reader.load_words(filename))
    # demo print
    print(len(english_words))
    new_wordlist = reader.reduce_list_to_only_five_letters(english_words)
    print(len(new_wordlist))
    new_wordlist = reader.eliminate_nonstandard_char_words(new_wordlist)
    print(len(new_wordlist))
    new_wordlist = reader.lowercase_all_words(new_wordlist)
    print(len(new_wordlist))
    print(new_wordlist)

#wordlist git repo location: 
# https://raw.githubusercontent.com/dwyl/english-words/master/words.txt

import urllib.request
import time

url = "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"
output_name = "words_alpha.txt"

def download_and_overwrite_wordlist(output_name = output_name):
    local_filename = output_name
    english_list = []
    for line in urllib.request.urlopen(url):
        english_list.append(line)
    
    overwrite_current_wordlist(local_filename, english_list)
    return local_filename

def overwrite_current_wordlist(old_filepath, new_wordlist):
    #overwrites the current wordlist file (all the language, not just the five letter words)
    with open(old_filepath, "w") as file:
        #for 
        #[file.write(str(word)) for word in new_wordlist]
        for word in new_wordlist:
            str_word = word.decode("utf-8")
            file.write(str_word)
            
    
    

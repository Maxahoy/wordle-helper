#wordlist git repo location: 
# https://raw.githubusercontent.com/dwyl/english-words/master/words.txt

import os
import shutil
import requests

url = "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"
output_name = "words_alpha.txt"

def download_wordlist():
    local_filename = output_name
    with requests.get(url, stream=True) as r:
        with open(output_name, "wb") as f:
            shutil.copyfileobj(r.raw, r)

    return local_filename
    
import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper():
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) >> 0:
        yn = input("Did you mean {} instead? Enter Y if yes, or N if no: ".format(get_close_matches(word, data.keys())[0]))
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "Ther word doesn't exits. Please doble check it."
        else:
            return "We did'nt understand your entry."
    else:
        return "The word doesn't exist. Please doble check it."

word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)


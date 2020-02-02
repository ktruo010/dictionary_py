import json
from difflib import get_close_matches

data = json.load(open("./data.json"))

def define(word):
    if word == "\end":
        return "Bye!"
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        confirm = input(f"Did you mean {get_close_matches(word, data.keys())[0]}? If so, enter Y or N for no.")
        if confirm == "Y" or confirm == "y":
            correctWord = get_close_matches(word, data.keys())[0]
            return data[correctWord]
        else:
            return ["Unfortunately, that word does not exist."]
    else:
        return ["Unfortunately, that word does not exist."]


while True:
    current_definition=""
    word = input("Enter word: ").lower()
    if word == "\end":
        break
    else:
        for definition in define(word):
            current_definition = current_definition + "\n" + definition + "\n"
        print(current_definition)
        continue
        

print(define(word))
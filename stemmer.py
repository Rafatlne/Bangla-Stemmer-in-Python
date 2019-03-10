import re

def stemmingSentence(firstText):
    print(firstText)
    for word in re.compile("[\\s।%,ঃ]+").split(firstText):
        print(word)

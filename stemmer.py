import re

lines = list()
passed = list()
CURLY_OPEN = "{"
CURLY_CLOSE = "}"
st = set()
file = open("common.rules","r")

def RuleFileParser(file):
    replaceRule = dict()

def whiteSpaceTrim(str):
    return re.sub("[\t' ']+","",str)

def commentTrim(str):

    return re.sub("#.*", "",str)

def extractReplaceRule(str):
    l = list()
    matches = re.search(".*->.*",str)
    if matches:
        l.append(re.compile("->").split(str))
        return l[1]
    else:
        return ""


def dependantCharSetInstallation():
    st.add('া')
    st.add('ি')
    st.add('ী')
    st.add('ে')
    st.add('ু')
    st.add('ূ')
    st.add('ো')

def stemmingSentence(firstText):
    print(firstText)
    for word in re.compile("[\\s।%,ঃ]+").split(firstText):
        print(word)



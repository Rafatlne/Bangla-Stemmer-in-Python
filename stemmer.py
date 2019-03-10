import re

replaceRule = dict()
lines = list()
newLines = list()
passed = list()
tempList = list()
CURLY_OPEN = "{"
CURLY_CLOSE = "}"
st = set()


def RuleFileParser(file):

    singleLine = file.readline()

    while singleLine:
        singleLine = whiteSpaceTrim(singleLine)
        singleLine = commentTrim(singleLine)

        if not singleLine: continue

        replace = extractReplaceRule(singleLine)
        singleLine = re.sub("->.*", "", singleLine)

        if not replace:
            replaceRule[singleLine] = [replace]
        lines.append(singleLine)
        singleLine = file.readline()

    file.close()
    lines.remove("\n")

    for word in lines:
        newLines.append(re.sub("[\n]",'',word))
    j=0
    for i in range(0,len(newLines)):
        if newLines[i] == '{':
            while newLines[i] != '}':
                i += 1
                if ( newLines[i] != ''):
                    tempList.append(newLines[i])
            tempList.remove('}')
            passed.append(tempList[:])
            del tempList[:]

    return passed




def whiteSpaceTrim(str):
    return re.sub("[\t' ']+","",str)


def commentTrim(str):
    return re.sub("#.*", "",str)


def extractReplaceRule(str):
    l = list()
    matches = re.search(".*->.*",str)
    if matches:
        a = re.compile("->").split(str)
        l.append(a)
        return l[0]
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

file = open("common.rules", "r")
print(RuleFileParser(file))
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
    dependantCharSetInstallation()
    singleLine = file.readline()

    while singleLine:
        singleLine = whiteSpaceTrim(singleLine)
        singleLine = commentTrim(singleLine)

        if not singleLine: continue

        replace = extractReplaceRule(singleLine)
        singleLine = re.sub("->.*", "", singleLine)
        singleLine = singleLine.rstrip("\n")

        if replace != "":
            replaceRule[singleLine] = [replace]

        lines.append(singleLine)
        singleLine = file.readline()

    file.close()

    j = 0
    for i in range(0, len(lines)):
        if lines[i] == '{':

            while lines[i] != '}':
                i += 1
                tempList.append(lines[i])

            tempList.remove('}')
            passed.append(tempList[:])
            del tempList[:]


def whiteSpaceTrim(str):
    return re.sub("[\t' ']+", "", str)


def commentTrim(str):
    return re.sub("#.*", "", str)


def extractReplaceRule(str):
    matches = re.search(".*->.*", str)
    if matches:
        a = re.split("->", str)
        return a[0]
    else:
        return ""


def stemOfWord(word):
    for i in range(0, len(passed)):
        for j in range(0, len(passed[i])):
            replacePrefix = passed[i][j]
            matcher = ".*" + replacePrefix + "$"
            if matcher in word:
                indx = len(word) - len(replacePrefix)
                if replacePrefix in replaceRule:
                    replaceSuffix = replaceRule.get(replacePrefix)
                    builder = word
                    l = 0
                    k = indx
                    for k in range(indx, len(replaceSuffix) + indx):
                        if replaceSuffix[l] != '.':
                            builder[k] = replaceSuffix[l]
                        k, l = k + 1, l + 1

                    word = builder[0:k]
                elif check(word[0:indx]):
                    word = word[0, indx]
                break
    return word


def dependantCharSetInstallation():
    st.add('া')
    st.add('ি')
    st.add('ী')
    st.add('ে')
    st.add('ু')
    st.add('ূ')
    st.add('ো')



def check(word):
    wordLength = 0
    for i in range(0, len(word)):
        if word[i] in st:
            continue
        wordLength += 1
    return wordLength >= 1


def stemmingSentence():
    firstText = open("inputfile", "r")
    singleLine = firstText.readline()
    print(singleLine)

    for word in re.split("[\\s।%,ঃ]+", singleLine):
        print(stemOfWord(word))

    firstText.close()


file = open("common.rules", "r")

# print(RuleFileParser(file))
RuleFileParser(file)
stemmingSentence()

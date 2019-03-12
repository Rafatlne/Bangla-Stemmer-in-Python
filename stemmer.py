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



    for i in range(0, len(lines)):
        if lines[i] == '{':
            i += 1
            while lines[i] != '}':
                if (lines[i] != ''):
                    tempList.append(lines[i])
                i += 1
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
            if re.search(matcher, word):
                indx = len(word) - len(replacePrefix)
                if replacePrefix in replaceRule:
                    replaceSuffix = replaceRule.get(replacePrefix)
                    replaceSuffix = "".join(replaceSuffix)
                    builder = list(word)
                    print(builder)
                    l = 0
                    kValue = 0
                    for k in range(indx, len(replaceSuffix) + indx):
                        if replaceSuffix[l] != '.':
                            builder[k] = replacePrefix[l]
                        l = l + 1
                        kValue = k+1
                    word = "".join(builder[0:kValue])
                elif check(word[0:indx]):
                    word = word[0:indx]
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


def stemmingSentence(text):
    singleLine = text.readline()

    while singleLine:
        print(singleLine)
        for word in re.split("[\\s।%,ঃ]+", singleLine):
            print(stemOfWord(word),end=" ")
        singleLine = text.readline()



commonRules = open("common.rules", "r")
inputfile = open("inputfile", "r")


RuleFileParser(commonRules)
stemmingSentence(inputfile)
commonRules.close()
inputfile.close()

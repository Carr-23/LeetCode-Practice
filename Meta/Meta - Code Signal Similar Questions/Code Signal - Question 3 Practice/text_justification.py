class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        curWidthLeft = maxWidth
        wordList = []
        returnList = []
        i = 0
        while i <= len(words):
            if i != len(words):
                w = words[i]

            if wordList and curWidthLeft - len(w) - 1 >= 0:
                print(w)
                print("here")
                wordList.append(w)
                curWidthLeft -= len(w) + 1
                i += 1
            elif not wordList and curWidthLeft - len(w) >= 0:
                print(w)
                print("here1")
                wordList.append(w)
                curWidthLeft -= len(w)
                i += 1
            else:
                spacesPer = (curWidthLeft + len(wordList) - 1) // max(
                    1, len(wordList) - 1
                )
                extraSpaces = curWidthLeft % max(1, len(wordList) - 1)
                print("spaces: " + str(spacesPer))
                string = ""
                if len(wordList) != 1:
                    for j in range(len(wordList) - 1):
                        wrd = wordList[j]
                        string += wrd + " " * spacesPer
                        if j < extraSpaces:
                            string += " "
                    string += wordList[-1]
                else:
                    string += wordList[0] + " " * curWidthLeft

                wordList = []
                curWidthLeft = maxWidth

                returnList.append(string)

        return returnList

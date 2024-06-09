from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        requiredCharsInLine = 0
        wordsInLine = 0
        curWordIndex = 0
        rv = []

        while(curWordIndex < len(words)):
            while((curWordIndex+wordsInLine < len(words)) and maxWidth - requiredCharsInLine >= (len(words[curWordIndex+wordsInLine]) if wordsInLine == 0 else (len(words[curWordIndex+wordsInLine]) + 1))):
                requiredCharsInLine += len(words[curWordIndex+wordsInLine]) if wordsInLine == 0 else (len(words[curWordIndex+wordsInLine]) + 1)
                wordsInLine += 1
            index = len(rv)
            rv.append("")
            for i in range(wordsInLine):
                if(i != 0):
                    rv[index] += " "
                rv[index] += words[i+curWordIndex]
            curWordIndex += wordsInLine 
            spacesRemaining = maxWidth - len(rv[index])
            i = 0
            justInserted = False
            if(curWordIndex != len(words) and wordsInLine != 1):
                while(spacesRemaining > 0):
                    if(not justInserted and rv[index][i] == " "):
                        rv[index] = rv[index][:i] + " " + rv[index][i:]
                        spacesRemaining -= 1
                        justInserted = True
                    if(rv[index][i] != " "):
                        justInserted = False
                    i = (i + 1)%len(rv[index])
            else:
                rv[index] += spacesRemaining * " "
            wordsInLine = 0
            requiredCharsInLine = 0
        return rv
s = Solution()
print(s.fullJustify(["What","must","be","acknowledgment","shall","be"], 16))
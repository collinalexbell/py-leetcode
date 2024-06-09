import math
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        completion = numRows + (numRows-2)
        if(completion == 0):
            return s
        result = []
        for i in range(numRows):
            result.append([])
        for i in range(len(s)):
            positionInCompletion = i%completion
            if(positionInCompletion < numRows):
                result[positionInCompletion].append(s[i])
            else:
                lastIndex = numRows-1
                indexIntoDiagnal = (positionInCompletion-numRows)
                result[lastIndex - indexIntoDiagnal - 1].append(s[i])

        return "".join(sum(result, []))
#[[]
# []
# []
# []]

# A
# B   F
# C E
# D 
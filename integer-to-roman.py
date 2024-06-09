toInt = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
                   }
order = ["M","D", "C", "L", "X", "V", "I"]

class Solution:
    def intToRoman(self, num: int) -> str:
        rv = ""
        for i in range(len(order)):
            if(i%2 == 0):
                # power of 10
                while(num - toInt[order[i]] >= 0):
                    rv += order[i]
                    num -= toInt[order[i]]
            else:
                    if(num-toInt[order[i]] >= 0):
                        rv += order[i]
                        num -= toInt[order[i]]

            # try a subtractive form
            if(i+1 < len(order) and num - toInt[order[i]] + toInt[order[i-i%2+2]] >= 0):
                    rv += order[i-i%2+2]
                    num += toInt[order[i-i%2+2]]
                    rv += order[i]
                    num -= toInt[order[i]]
        return rv

s = Solution()
print(s.intToRoman(3749))
print(s.intToRoman(58))
print(s.intToRoman(1994))
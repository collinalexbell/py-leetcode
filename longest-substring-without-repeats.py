class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s) == 0):
            return 0
        seen = set()
        length = 1
        start = 0
        longestSubstring = 0

        while(start+length-1 < len(s)):
            lastIndex = start+length-1
            if(s[lastIndex] in seen):
                seen.remove(s[start])
                start += 1
                length -= 1
            else:
                if(length > longestSubstring):
                    longestSubstring = length
                seen.add(s[lastIndex])
                length = length + 1
        return longestSubstring
s = Solution()
print(s.lengthOfLongestSubstring("dvdf"))
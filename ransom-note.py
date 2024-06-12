class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        availableLetters = {}
        for letter in magazine:
            if(letter not in availableLetters):
                availableLetters[letter] = 1
            else:
                availableLetters[letter] += 1
        for letter in ransomNote:
            if letter not in availableLetters or not availableLetters[letter] > 0:
                return False
            else:
                availableLetters[letter] -= 1
        return True
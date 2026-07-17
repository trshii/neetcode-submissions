class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        seen2 = {}
        for letter in s:
            if letter not in seen:
                seen[letter] = 1
            else:
                seen[letter] += 1
        for letter in t:
            if letter not in seen2:
                seen2[letter] = 1
            else:
                seen2[letter] += 1
        return seen == seen2
        
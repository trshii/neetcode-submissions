class Solution:
    def scoreOfString(self, s: str) -> int:
        len_s = len(s)
        score = 0
        for i in range(1, len_s):
            score += abs(
                ord(s[i]) - ord(s[i-1])
            )

        return score
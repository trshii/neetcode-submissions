class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l_ptr, r_ptr = 0, 0
        len_s, len_t = len(s), len(t)

        while (l_ptr < len_s and r_ptr < len_t):
            if (s[l_ptr] == t[r_ptr]):
                l_ptr += 1
                r_ptr += 1
            else:
                r_ptr += 1
        
        return l_ptr == len_s
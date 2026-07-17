class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        len_t = len(t)
        len_s = len(s)
        left_ptr, right_ptr = 0, 0

        while (left_ptr < len_s and right_ptr < len_t):
            if (s[left_ptr] == t[right_ptr]):
                left_ptr += 1
                right_ptr += 1
            else:
                left_ptr += 1

        return len_t - right_ptr
        


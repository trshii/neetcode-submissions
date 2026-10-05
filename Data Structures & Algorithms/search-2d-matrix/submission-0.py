class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r0, rl = 0, len(matrix)-1
        
        def _bin_col(idx: int) -> bool:
            m_row = matrix[idx]
            l, r = 0, len(m_row)-1
            while l <= r:
                m = (l+r)//2
                if m_row[m] == target:
                    return True
                elif m_row[m] < target:
                    l = m+1
                else:
                    r = m-1
            return False

        while r0 <= rl:
            m = (r0 + rl)//2
            if _bin_col(m):
                return True
            elif matrix[m][0] < target:
                r0 = m+1
            else:
                rl = m-1
        return False
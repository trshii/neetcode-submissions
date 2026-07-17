class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}
        for s in strs:
            fz_s = tuple(sorted(s))
            
            if fz_s not in grouped:
                grouped[fz_s] = [s]
            else:
                grouped[fz_s].append(s)

        out = list(grouped.values())
        return out
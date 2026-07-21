from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = [[] for _ in range(len(nums) + 1)]

        for n, c in count.items():
            freq[c].append(n)

        out = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                out.append(n)
                if len(out) == k:
                    return out


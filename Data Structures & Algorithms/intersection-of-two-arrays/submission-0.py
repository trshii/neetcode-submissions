class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set, nums2_set = set(nums1), set(nums2)

        out = []

        for num in nums1_set:
            if num in nums2_set:
                out.append(num)

        return out
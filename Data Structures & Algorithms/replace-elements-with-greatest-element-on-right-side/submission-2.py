class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        len_arr = len(arr)
        right_max = -1
        for i in range(len_arr - 1, -1, -1):
            arr[i], right_max = right_max, max(right_max, arr[i])

        return arr


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        len_arr = len(arr)
        right_max = -1
        for i in range(len_arr - 1, -1, -1):
            pot_max = arr[i]
            arr[i] = right_max
            right_max = max(right_max, pot_max)

        return arr


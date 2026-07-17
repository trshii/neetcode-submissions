class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        len_arr = len(arr)
        for i in range(len_arr - 1):
            arr[i] = max(arr[i+1:])

        arr[len_arr - 1] = -1

        return arr

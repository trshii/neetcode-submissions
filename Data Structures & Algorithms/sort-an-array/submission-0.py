class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def _mergeSort(nums: List[int], l: int, r: int) -> None:
            if l >= r:
                return

            mid = (l + r) // 2
            _mergeSort(nums, l, mid)
            _mergeSort(nums, mid + 1, r)

            i, j, res = l, mid + 1, []
            
            while i <= mid and j <= r:
                if nums[i] <= nums[j]:
                    res.append(nums[i])
                    i += 1
                else:
                    res.append(nums[j])
                    j += 1

            nums[l:r+1] = res + nums[i:mid + 1] + nums[j:r + 1]

        _mergeSort(nums, 0, len(nums) - 1)
        return nums
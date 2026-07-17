class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        low = 0
        high = len(nums) - 1
        result = -1

        while low <= high:
            mid = (high + low) // 2

            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                result = mid
                break

        return result

        
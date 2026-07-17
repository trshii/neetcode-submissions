class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        output_list = []
        for _ in range(2):
            for item in nums:
                output_list.append(item)

        return output_list

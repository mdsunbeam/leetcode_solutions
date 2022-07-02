class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        for key, value in enumerate(nums):
            difference = target - value
            if difference in ans:
                return [ans[difference], key]
            ans[value] = key
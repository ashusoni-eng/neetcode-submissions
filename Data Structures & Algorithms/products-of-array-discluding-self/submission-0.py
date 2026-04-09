class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        length = len(nums)

        for i in range(length):
            res = 1
            for j in range(length):
                if j == i:
                    continue
                res = res * nums[j]
            result.append(res)
        return result
        
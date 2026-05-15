class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        arr = list(range(1, n))
        arr.append(n - 1)
        if nums == arr:
            return True
        return False

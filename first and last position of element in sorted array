class Solution:
    def searchRange(self, nums, target):
        def lowerBound(arr, target):
            low, high = 0, len(arr) - 1
            ans = len(arr)
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] >= target:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return ans

        def upperBound(arr, target):
            low, high = 0, len(arr) - 1
            ans = len(arr)
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] > target:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return ans

        first = lowerBound(nums, target)
        last = upperBound(nums, target) - 1

        # check if it exists
        if first <= last and first < len(nums) and nums[first] == target:
            return [first, last]
        return [-1, -1]

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        jump=0
        for i in range (0,n):
            if i>jump:
                return False
            jump=max(jump,i+nums[i])
            if jump >=n-1:
                return True 
        return jump>=n-1
        

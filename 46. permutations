class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def generate(subset,ans,nums):
            if(len(subset)==len(nums)):
                ans.append(subset.copy()) 
                return 
            for num in nums:
                if(num not in subset):
                    subset.append(num) 
                    generate(subset,ans,nums) 
                    subset.pop()
        ans = [] 
        subset = [] 
        generate(subset,ans,nums) 
        return ans 

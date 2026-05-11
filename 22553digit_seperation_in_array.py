class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        arr=[]
        for i in nums:
            s=str(i)
            for j in s:
                arr.append(int(j))
        return arr

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root :
            return []
        res=[]
        queue=[root]
        while queue:
            res.append(queue[-1].val) 
            new=[]
            for i in queue:
                if i.left:
                    new.append(i.left)
                if i.right :
                    new.append(i.right)
            queue=new 
        return res   


           

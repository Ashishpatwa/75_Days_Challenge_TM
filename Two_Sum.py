class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        for x,i in enumerate(nums):
            if i in d:
                d[i]=x
            else:
                d[i]=x
        
        for x,i in enumerate(nums):
            if target-i in d and d[target-i] !=x:
                return [x,d[target-i]]
        return [-1,-1]
                
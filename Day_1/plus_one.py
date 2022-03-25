class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        prev=1
        for i in range(len(digits)-1,-1,-1):
            k = (digits[i]+prev)
            prev = k/10
            digits[i]=k%10
            if prev==0:
                break
        if prev!=0:
            digits.insert(0,prev)
                
            
        return digits
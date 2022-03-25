class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        p1,p2=0,0
        mx=0
        for i in range(len(prices)):
            p2=i
            if prices[p2]<prices[p1]:
                p1=p2
            elif prices[p2]>prices[p1]:
                mx=max(mx,prices[p2]-prices[p1])
        return mx
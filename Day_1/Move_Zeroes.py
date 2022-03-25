p1=0
        p2=0
       
        
        while p2<len(nums)and p1<=p2:
            if nums[p1]!=0:
                p1+=1
                p2=p1
            elif nums[p2]==0:
                p2+=1
            else:
                nums[p1],nums[p2]=nums[p2],nums[p1]
                p1+=1
                p2+=1
        return nums
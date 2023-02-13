class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[]
        pref_prod=None
        num_zero=0
        for num in nums:
            if num !=0 and pref_prod==None:
                pref_prod=num
            elif num!=0:
                pref_prod*=num
            elif num==0:
                num_zero+=1
        if num_zero>1:
            ans=[0]*len(nums)
        elif num_zero==1:
            for num in nums:
                if num !=0:
                    ans.append(0)
                else:
                    ans.append(pref_prod)
        else:
            for num in nums:
                ans.append(pref_prod//num)
        return ans
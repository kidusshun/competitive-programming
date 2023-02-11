class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start=0
        output=0
        for i in range(len(nums)):
            if nums[i]==0:
                k-=1
            while k<0:
                if nums[start]==0:
                    k+=1
                start+=1
            output=max(output,i-start+1)
        return output
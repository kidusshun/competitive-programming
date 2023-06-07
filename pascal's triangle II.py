class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        arr=[1]
        def helper(prev,level,ind):
            if ind+1==level:
                return prev
            arr=[1]*(level+1)
            l,r=0,1
            while r<len(prev):
                arr[r]=prev[l]+prev[r]
                l+=1
                r+=1
            return helper(arr,level+1,ind)
        if rowIndex==0:
            return arr
        else:
            return helper(arr,0,rowIndex)
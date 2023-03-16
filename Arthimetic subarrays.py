class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        m=len(r)
        ans=[]
        bool_val=True
        count=0
        while count < m:
            new_nums=nums[l[count]:r[count]+1]
            new_nums.sort()
            difference=None
            for i in range(len(new_nums)-1):
                diff=new_nums[i+1]- new_nums[i]
                if difference ==None:
                    difference=diff
                elif difference==diff:
                    continue
                else:
                    bool_val=False
                    break
            count+=1
            ans.append(bool_val)
            bool_val=True
        return ans
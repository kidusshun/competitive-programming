class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        length = len(nums)
        valid = True
        start_sign = True
        for i in range(length):
            seen = set()
            if nums[i]<0:
                start_sign = False
            else:
                start_sign = True
            valid = True
            seen.add(i)
            j = (nums[i]+i)%length
            if j != i:
                k=1
            else:
                continue
            while j not in seen:
                if (nums[j]>0 and start_sign == False) or (nums[j]<0 and start_sign == True):
                    valid= False
                    break
                seen.add(j)
                new_j = (nums[j]+j)%length
                if new_j != j:
                    k+=1
                else:
                    valid = False
                    break
                j=new_j
            if valid and k>1:
                return True
        return False
def numIdenticalPairs(nums):
        amount=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    amount+=1
        return amount
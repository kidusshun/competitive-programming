def rotate(nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        new=[]
        pointer=len(nums)-k
        for i in range(pointer,len(nums)):
            new.append(nums[pointer])
            pointer+=1
        for i in range(pointer-k):
            new.append(nums[i])
        nums=new
        print(nums)
rotate([-1,-100,3,99], 2)
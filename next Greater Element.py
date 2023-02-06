class Solution:
    def nextGreaterElement(self, nums1, nums2):
        arr=[]
        for a in nums1:
            ind=nums2.index(a)
            if ind==len(nums2)-1:
                arr.append(-1)
            else:
                while ind < len(nums2)-1:
                    if a < nums2[ind+1]:
                        arr.append(nums2[ind+1])
                        break
                    else:
                        arr.append(-1)
                        break
                    ind +=1
        return arr
new= Solution()
new.nextGreaterElement([1,3,5,2,4], [5,4,3,2,1])
        
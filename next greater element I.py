class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_index={n:i for i, n in enumerate((nums1))}
        result= [-1] * len(nums1)
        stack=[]

        for i in range(len(nums2)):
            current=nums2[i]
            while stack and current > stack[-1]:
                value = stack.pop()
                idx = nums1_index[value]
                result[idx]=current
            if current in nums1:
                stack.append(current)
        return result

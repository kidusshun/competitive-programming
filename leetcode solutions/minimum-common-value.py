class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1_pointer = 0
        nums2_pointer = 0
        while nums1_pointer <len(nums1) and nums2_pointer <len(nums2):
            if nums1[nums1_pointer] < nums2[nums2_pointer]:
                nums1_pointer+=1
            elif nums1[nums1_pointer] > nums2[nums2_pointer]:
                nums2_pointer+=1
            else:
                return nums1[nums1_pointer]
        return -1
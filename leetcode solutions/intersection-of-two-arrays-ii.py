class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = Counter(nums1)
        ans = []
        for num in nums2:
            if num in d:
                ans.append(num)
                d[num] -=1
                if d[num] == 0:
                    del d[num]
        return ans
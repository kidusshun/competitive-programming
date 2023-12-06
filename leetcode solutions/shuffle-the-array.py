class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i =0
        shuffled_array = []
        while n < len(nums):
            shuffled_array.append(nums[i])
            shuffled_array.append(nums[n])
            i+=1
            n+=1
        return shuffled_array
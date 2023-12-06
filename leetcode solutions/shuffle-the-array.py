class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i,j =0,n
        shuffled_array = []
        while j < len(nums):
            shuffled_array.append(nums[i])
            shuffled_array.append(nums[j])
            i+=1
            j+=1
        return shuffled_array
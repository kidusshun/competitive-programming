class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos_index, neg_index = 0,0
        length = len(nums)
        ans = []
        while pos_index<length and neg_index < length:
            while pos_index <length:
                if nums[pos_index] >0:
                    ans.append(nums[pos_index])
                    pos_index+=1
                    break
                pos_index+=1
            while neg_index <length:
                if nums[neg_index] <0:
                    ans.append(nums[neg_index])
                    neg_index+=1
                    break
                neg_index+=1
        return ans
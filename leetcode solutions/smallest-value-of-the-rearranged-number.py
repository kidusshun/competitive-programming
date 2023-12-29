class Solution:
    def smallestNumber(self, num: int) -> int:
        nums = [char for char in str(num)]
        if num == 0:
            return num
        if num>0:
            nums.sort()
            if nums[0] == '0':
                for i in range(len(nums)):
                    if nums[i] != "0":
                        nums[i],nums[0] = nums[0],nums[i]
                        break
            return int("".join(nums))
        else:
            nums = sorted(nums[1:], reverse = True)
            return -1 * int("".join(nums))
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = sum(arr)
        length = len(arr)
        
        for i in range(3, length+1, 2):
            l = 0
            r = i

            while r <= length:
                ans += sum(arr[l:r])
                l+=1
                r+=1
        return ans
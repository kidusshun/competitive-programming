class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count=0
        sum=0
        min_sum=k*threshold
        for i in range(len(arr)):
            sum+=arr[i]
            if i <(k -1):
                continue
            if i>(k-1):
                sum-=arr[i-k]
            if sum>=min_sum:
                count+=1
        return count
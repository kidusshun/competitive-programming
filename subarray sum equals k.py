class Solution:
    def subarraySum(self, nums, k) -> int:
        result=0
        prefix_sum=0
        dict={0:1}
        for num in nums:
            prefix_sum += num
            if prefix_sum-k in dict:
                result = result + dict[prefix_sum-k]
            dict[prefix_sum] = dict.get(prefix_sum,0)+1
        return result
st=[0,1,2,3,4,5]
print(st[0:1])
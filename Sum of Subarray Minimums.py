class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        left = [-1]*len(arr)
        right = [len(arr)]*len(arr)
        for i in range(len(arr)):
            while stack and arr[i] <= arr[stack[-1]]:
                tmp = stack.pop()
                right[tmp] = i
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        res = 0
        for cur, (a,b) in enumerate(zip(left,right)):
            res += arr[cur]*(b-cur)*(cur-a)
        return res%(10**9+7)
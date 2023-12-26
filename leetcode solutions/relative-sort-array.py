class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = [0]*(max(arr1)+1)
        for i in range(len(arr1)):
            count[arr1[i]] +=1
        print(count)
        ans = []
        seen = set()
        for num in arr2:
            for _ in range(count[num]):
                ans.append(num)
                seen.add(num)
        for i in range(len(count)):
            if i not in seen:
                for _ in range(count[i]):
                    ans.append(i)
        return ans
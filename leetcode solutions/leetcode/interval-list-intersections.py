class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = 0
        ans = []
        for left, right in firstList:
            i = 0
            while i<len(secondList):
                if left <= secondList[i][0] <= right:
                    ans.append([secondList[i][0],min(right, secondList[i][1])])
                elif left <= secondList[i][1]<=right:
                    ans.append([left, min(right, secondList[i][1])])
                elif secondList[i][0] <= left <= right and secondList[i][0]<=right<=secondList[i][1] :
                    ans.append([left,right])
                i+=1
        return ans
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict_1 = {}
        index_sum = float("inf")
        ans = []
        for i, val in enumerate(list2):
            dict_1[val] = i
        
        for i,string in enumerate(list1):
            if string in list2:
                pos = dict_1[string]
                curr_sum = pos+i
                if curr_sum < index_sum:
                    index_sum = pos + i
                    ans = [string]
                elif curr_sum == index_sum:
                    ans.append(string)
        return ans
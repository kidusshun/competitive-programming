class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        def validate(s_dict, t_dict):
            for key in t_dict:
                if s_dict[key] and s_dict[key] >= t_dict[key]:
                    continue
                else:
                    return False
            return True
        t_dict = Counter(t)
        s_dict = defaultdict(int)
        l = 0
        ans = ""
        ans_length = float("inf")
        for r in range(len(s)):
            s_dict[s[r]]+=1
            while validate(s_dict,t_dict):
                if r-l+1 < ans_length:
                    ans_length = r-l+1
                    ans = s[l:r+1]
                s_dict[s[l]] -=1
                l+=1
        return ans
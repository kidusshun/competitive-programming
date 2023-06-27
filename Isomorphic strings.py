class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map ={}
        t_map = {}

        for i in range(len(t)):
            if s[i] not in s_map.keys() and t[i] not in t_map.keys():
                s_map[s[i]]=t[i]
                t_map[t[i]]=s[i]
            elif s[i] not in s_map.keys() and t[i] in t_map.keys():
                return False
            elif t[i] not in t_map.keys() and s[i] in s_map.keys():
                return False
            elif s_map[s[i]] == t[i] and t_map[t[i]] == s[i]:
                continue
            else:
                return False
        return True
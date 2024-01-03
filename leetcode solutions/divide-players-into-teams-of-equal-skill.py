class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left,right = 1,len(skill)-2
        skill_to_match = skill[0]+skill[-1]
        chemistry_sum = skill[-1]*skill[0]

        while left<right:
            if skill[left]+skill[right] != skill_to_match:
                return -1
            else:
                chemistry_sum+=(skill[left]*skill[right])
            left+=1
            right-=1
        
        return chemistry_sum
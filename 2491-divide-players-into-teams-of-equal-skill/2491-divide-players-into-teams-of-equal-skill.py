class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        i = 0
        mid = len(skill) //2
        chemistry = 0 
        sum_req = skill[0] + skill[-1]
        
        while i < mid:
            temp = skill[i] + skill[len(skill) - i -1]
            if temp == sum_req:
                chemistry += skill[i] * skill[len(skill) - i -1]
            else:
                return -1
            
            i += 1
        
        return chemistry
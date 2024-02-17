class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        beginning_to_end = abs(target[0]) + abs(target[1])

        for i, j in ghosts:
            if abs(i-target[0]) + abs(j-target[1]) <= beginning_to_end:
                return False
        return True
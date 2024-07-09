from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        dead_set = set(deadends)
        if "0000" in dead_set:
            return -1
        
        q = deque([('0000', 0)])  # (current, steps)
        seen = set('0000')
        
        while q:
            current, steps = q.popleft()
            
            if current == target:
                return steps
            
            for i in range(4):
                for move in [-1, 1]:
                    new_digit = (int(current[i]) + move) % 10
                    new_comb = current[:i] + str(new_digit) + current[i+1:]
                    
                    if new_comb not in seen and new_comb not in dead_set:
                        seen.add(new_comb)
                        q.append((new_comb, steps + 1))
        
        return -1

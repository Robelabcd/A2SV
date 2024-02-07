class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        count = 0
        for op in operations:
            if op == 'X--' or op == '--X':
                count -= 1
            if op == 'X++' or op == '++X':
                count += 1
        return count   
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for element in logs:
            if element.startswith('../'):
                if stack:
                    stack.pop()
            elif element.startswith('./'):
                continue
            else:
                stack.append(element)

        return len(stack)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        a = ""
        for i in digits:
           a = a + str(i)
        b = str(int(a) + 1)
        result = []
        for i in b:
            result.append(int(i))

        return result


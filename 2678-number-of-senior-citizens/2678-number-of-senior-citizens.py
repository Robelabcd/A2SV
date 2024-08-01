class Solution:
    def countSeniors(self, details: List[str]) -> int:
        
        count = 0
        for element in details:

            if int(element[11:13]) > 60:
                count += 1

        return count
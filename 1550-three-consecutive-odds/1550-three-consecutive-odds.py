class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        
        count = 0
        for ele in arr:

            if ele % 2 == 1:
                count += 1

                if count == 3:
                    return True

            else:
                count = 0

        return False

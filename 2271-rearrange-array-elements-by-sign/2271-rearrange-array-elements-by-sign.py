class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []

        for num in nums:
            if num >= 0:
                positive.append(num)
            else:
                negative.append(num)

        result = []

        i, j = 0, 0
        while i < len(positive) and j < len(negative):
            
            result.append(positive[i])
            result.append(negative[j])
            i += 1
            j += 1

        result.extend(negative[j:])
        result.extend(positive[i:])

        return result
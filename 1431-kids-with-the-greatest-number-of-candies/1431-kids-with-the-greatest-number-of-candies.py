class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        maxx = max(candies)
        for candy_per_kid in candies:
            curr = candy_per_kid + extraCandies
            if curr <  maxx:
                result.append(False)
            else:
                result.append(True)

        return result

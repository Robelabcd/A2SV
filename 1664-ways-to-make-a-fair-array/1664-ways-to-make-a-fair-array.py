class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_odd = [0] * (n + 1)
        prefix_even = [0] * (n + 1)
        count = 0

        for i in range(n):
            prefix_odd[i + 1] = prefix_odd[i]
            prefix_even[i + 1] = prefix_even[i]
            if i % 2 == 0:
                prefix_even[i + 1] += nums[i]
            else:
                prefix_odd[i + 1] += nums[i]

        for i in range(n):
            odd_sum = prefix_odd[i] + prefix_even[n] - prefix_even[i + 1]
            even_sum = prefix_even[i] + prefix_odd[n] - prefix_odd[i + 1]
            if odd_sum == even_sum:
                count += 1

        return count

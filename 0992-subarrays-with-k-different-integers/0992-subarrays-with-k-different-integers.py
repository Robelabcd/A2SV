class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(nums, k):
            count = 0
            lp = 0
            store = {}

            for rp in range(len(nums)):
                store[nums[rp]] = rp

                if len(store) > k:
                    Tremoved = min(store.values())
                    lp = Tremoved + 1
                    del store[nums[Tremoved]]

                count += rp - lp + 1

            return count

        return atMostK(nums, k) - atMostK(nums, k - 1)

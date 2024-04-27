class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        dp = [[-1 for _ in range(len(key))] for _ in range(len(ring))]
        return self.solve(ring, 0, key, 0, dp)

    def solve(self, ring, curr, key, key_index, dp):
        if key_index == len(key):
            return 0

        if dp[curr][key_index] != -1:
            return dp[curr][key_index]

        min_ans = float('inf')
        for i in range(len(ring)):
            if ring[i] == key[key_index]:
                steps_between = abs(i - curr)
                steps_around = len(ring) - steps_between
                min_steps = min(steps_between, steps_around)
                min_steps += self.solve(ring, i, key, key_index + 1, dp) + 1
                min_ans = min(min_steps, min_ans)

        dp[curr][key_index] = min_ans
        return min_ans

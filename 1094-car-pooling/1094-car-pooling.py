class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        prefix_sum = [0]*(10001)

        for i in range(len(trips)):

            each_capacity = trips[i][0]
            left = trips[i][1]
            right = trips[i][2]

            prefix_sum[left] += each_capacity
            prefix_sum[right] -= each_capacity if right < len(prefix_sum) else 0

        print(prefix_sum)

        cum_sum = [0]*(10001)
        cum_sum[0] = prefix_sum[0]

        for i in range(1, len(cum_sum)):
            cum_sum[i] = cum_sum[i-1] + prefix_sum[i]

        print(cum_sum)
        for i in range(len(cum_sum)):
            if capacity < cum_sum[i]:
                return False

        return True


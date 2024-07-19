class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    
        #pair programming

        sumGas = sum(gas)
        sumCost = sum(cost)

        if sumCost > sumGas:
            return -1
        
        ans = 0
        curr = 0
        
        for i in range(len(gas)):
            curr += gas[i] - cost[i]

            if curr < 0:
                curr = 0
                ans = i + 1
        
        return ans
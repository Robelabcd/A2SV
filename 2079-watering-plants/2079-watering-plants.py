class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        count = 0
        original_capacity = capacity

        for i in range(len(plants)):
            if capacity>=plants[i]:
                count += 1
                capacity = capacity-plants[i]
            else:
                count = count+((2*i)+1)
                capacity = original_capacity
                capacity = capacity-plants[i]
        
        return count
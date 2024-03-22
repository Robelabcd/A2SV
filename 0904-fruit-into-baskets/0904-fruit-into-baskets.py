class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        lp = 0
        count = 0
        basket = {}

        for rp in range(len(fruits)):
            
            #store the new fruit or the updated position of the fruit that's already there
            basket[fruits[rp]] = rp


            #check if the basket contains more than two
            if len(basket) > 2:

                fruit_to_be_removed = min(basket.values())
                lp = fruit_to_be_removed + 1
                del basket[fruits[fruit_to_be_removed]]

            count = max(count, rp-lp+1)

        return count
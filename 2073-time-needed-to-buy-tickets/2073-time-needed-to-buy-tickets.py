class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        for i in range(k):

            if tickets[i] < tickets[k]:
                count += tickets[i]

            else:
                count += tickets[k]

        print(count)
        if len(tickets)-1 > k:
            j = k+1
            while j < len(tickets):
                if tickets[j] < (tickets[k]-1):
                    count += tickets[j]

                else:
                    count += tickets[k]-1
                
                j+=1
            print(count)
            return count+tickets[k]

        else:
            return count + tickets[k]

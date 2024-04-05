class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        N = len(cardPoints)
        frd_prefix = [c for c in cardPoints]
        for i in range(1, N):
            frd_prefix[i] += frd_prefix[i-1] 
        
        back_prefix = [c for c in cardPoints]
        for i in range(N-2, -1, -1):
            back_prefix[i] += back_prefix[i+1]

        #back_prefix.reverse()
        from_front = frd_prefix[k-1]
        from_back = back_prefix[-k]
        
        print(frd_prefix)
        print(back_prefix)
        i, j = k-2, N-1
        maxx = max(from_front, from_back)
 
        while i >= 0:

            current = frd_prefix[i] + back_prefix[j]
            print(current)
            maxx = max(maxx, current)
            print(maxx)
            i -= 1
            j -= 1

        return maxx

            


        
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
        prefix = [0]*(n+1)

        for book in bookings:
            left = book[0] -1
            right = book[1]

            prefix[left] += book[2]
            prefix[right] -= book[2] 
        prefix.pop()
        
        for i in range(1, n):
            prefix[i] += prefix[i-1]

        return prefix


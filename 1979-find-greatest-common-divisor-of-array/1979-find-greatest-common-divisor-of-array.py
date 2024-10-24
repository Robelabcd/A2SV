class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minn = min(nums)
        maxx = max(nums)

        '''
        e.g: minn = 8, maxx = 16

        lcm = 16
        gcd = 8


        property for lcm and gcd

        gcd = a * b // lcm
        
        '''

        lcm = 1
        while True:

            if maxx * lcm % minn == 0:
                lcm = lcm * maxx
                break
            lcm += 1

        gcd = minn * maxx // lcm
        return gcd
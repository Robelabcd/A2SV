class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        pref_sum = [0]*(len(s)+1)

        for i in range(len(shifts)):
            left = shifts[i][0]
            right = shifts[i][1]
            direction = shifts[i][2]

            '''
            [0, 0], [0, 1, 1]
            [1, -1]
            
            
            '''

            if direction == 0:
                pref_sum[left] -= 1
                pref_sum[right+1] += 1 

            else:
                pref_sum[left] += 1
                pref_sum[right+1] -= 1 
            
        
        for i in range(1, len(pref_sum)):
            pref_sum[i] += pref_sum[i-1]

        ans = []

        for i in range(len(s)):

            index = ord(s[i]) - ord('a')
            shifted = pref_sum[i]
            temp = (index + shifted) % 26
            ans.append(chr(temp + ord('a')))
        
        return "".join(ans)
        
        # alpa = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

        # for i in range(len(s)):
        #     index = alpa.index(s[i]) + 26

        #     if cum_sum[i] < 0:
        #         temp = abs(cum_sum[i]) % 26
        #         res = (index - temp)
        #         ans.append(alpa[res])

        #     else:
        #         temp = cum_sum[i] % 26
        #         res = index + temp
        #         ans.append(alpa[res])

        # return "".join(ans)
            


        

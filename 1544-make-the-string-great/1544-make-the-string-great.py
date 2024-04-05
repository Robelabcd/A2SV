class Solution(object):
    def makeGood(self, s):
        
        ans = []
        for i in s:
            if ans and abs(ord(i)-ord(ans[-1]))==32:
                ans.pop()
            else:
                ans.append(i)
        return "".join(ans)
class Solution:
    def smallestNumber(self, num: int) -> int:
        postive=num>0
        ans=""
        num=sorted(str(abs(num)),reverse=not postive)
        zeros=0
        for i in num:
            if i=='0':
                zeros+=1
            else:
                ans+=i
        if postive:
            ans=ans[0]+('0'*zeros)+ans[1:]
        else:
            ans+='0'*zeros

        return int(ans)*pow(-1,1+postive)

            
            

        
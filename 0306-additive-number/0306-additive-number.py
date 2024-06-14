class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        n = len(num)
        # if num.startswith("0"):
        #     return False

        def helper(index, num1, num2):
            
            if index == n:
                return True
            
            # if num[index] == '0':
            #     return False
                

            for k in range(index+1, n+1):
                num3 = int(num[index:k])

                if num3 != 0 and num[index] == '0':
                    return False
            
                if num1 + num2 == num3:
                    return helper(k, num2, num3)

            return False
  

        for i in range(1, n):
            for j in range(i+1, n):
                x, y = num[:i], num[i:j]

                if  (len(y) > 1 and y.startswith("0")) or (len(x) > 1 and x.startswith("0")):
                    continue

                if helper(j, int(x), int(y)):
                    return True

        return False

        
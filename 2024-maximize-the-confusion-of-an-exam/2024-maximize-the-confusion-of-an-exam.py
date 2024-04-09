class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        def T_F(chars):

            left = res = 0
            count = k
            for right in range(len(answerKey)):

                if answerKey[right] != chars:
                    count -= 1

                while count < 0:
                    if answerKey[left] != chars:
                        count += 1
                    left += 1

                res = max(res, right-left+1)

            return res

        return max(T_F('T'), T_F('F'))


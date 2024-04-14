class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        #DO it again if you encounter this problem
        
        
        res = []
        dicts = {"2": "abc","3": "def","4": "ghi","5": "jkl","6": "mno","7": "pqrs","8": "tuv","9": "wxyz"}

        def combos_function(i, combo):
            if i >= len(digits):
                res.append(combo)
                return

            for c in dicts[digits[i]]:
                combos_function(i + 1, combo + c)

        if digits:
            combos_function(0, "")

        return res
  
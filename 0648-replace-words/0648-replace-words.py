class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        look = set(dictionary)
    
        def replace(word):
            for i in range(1, len(word) + 1):
                if word[:i] in look:
                    return word[:i]
            return word
    
        return ' '.join(map(replace, sentence.split()))
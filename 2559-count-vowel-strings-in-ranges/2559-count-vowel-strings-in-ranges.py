class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        '''
        [1, 0, 1, 1, 1]

        [1, 1, 2, 3, 4]
        '''
        vowel = 'aeiou'
        prefix = [0]*len(words)

        for i in range(len(words)):

            if words[i][0] in vowel and words[i][-1] in vowel:
                prefix[i] = 1

            else:
                prefix[i] = 0

        for i in range(1, len(prefix)):
            prefix[i] += prefix[i-1]

        # now we have [1, 1, 2, 3, 4]
        #let accept the queries

        ans = []
        for q in queries:
            l, r = q[0], q[1]

            ans.append(prefix[r] - prefix[l-1] if l > 0 else prefix[r])

        return ans
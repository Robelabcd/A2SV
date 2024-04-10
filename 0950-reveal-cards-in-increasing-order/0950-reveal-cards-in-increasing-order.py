class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        
        '''
        deck = [17, 13, 11, 2, 3, 5, 7]

        Rule: take card ---> jump the next card and append it to the end

        Goal: to find an increasing number of cards following the rule


        deck.sort() -----> [2, 3, 5, 7, 11, 13, 17]

        [2, jump, 3, jump, 5, jump, 7]
        [2, jump, 3, 11, 5, jump, 7]
        [2, 13, 3, 11, 5, jump, 7]
        [2, 13, 3, 11, 5, 17, 7] ---------------> result


        Use deque() - double ended queue data structure: to pop and append
        
        
        '''

        # sort the deck so that to add eack deck increasingly
        deck.sort()

        result = [0]*len(deck)   #initialize

        #let's create a deque that contains the index of the decks

        que = deque(range(len(deck)))    #(0 upto len(deck))


        for single_deck in deck:

            index = que.popleft()

            result[index] = single_deck

            #now the next index has to jumped

            if que:     #as long as true pop the next index and append it at the end
                i = que.popleft()
                que.append(i)     #or simply, que,append(que,popleft())


        return result

                



            












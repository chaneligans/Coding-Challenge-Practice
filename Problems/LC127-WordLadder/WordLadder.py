from collections import defaultdict
from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # we cannot transform to the word if it's not in the list, so end
        if endWord not in wordList:
            return 0
        
        L = len(beginWord)
        
        # defaultdict creates helps group key-value pairs into a dictionary of lists
        # example values: ('blue', [1, 2]), ('red', [1]), ('yellow', [3, 4, 5])
        # in this case: ('*it', [hit]), ('h*t', [hit, hot]), ('hi*', [hit])
        # HOWEVER, because 'hit' is the beginWord, it's not included in the wordList
        # therefore, an ex would be: ('*it', []), ('h*t', [hot]), ('hi*', [])
        combinations = defaultdict(list)
        
        
        # now iterate through every word in the list 
        for word in wordList:
            # add every word into their value
            # ex: add hot into h*t, add dot/lot into *ot
            for i in range(L):
                combinations[word[:i] + "*" + word[i+1:]].append(word)
                
                
        # deque is a kind of queue (double-ended queue) that allows u to popleft -> O(1) time!
        # this helps to keep track of what level (depth) we are in the BFS tree
        queue = deque([(beginWord, 1)])
        
        
        # using a set bc it's more efficient? sets don't do indexing or whatever
        # "an unordered collection"
        visited = set()
        visited.add(beginWord) # beginWord is the first word we start with, so init with it
        
        
        # continue looping until we've visited every node
        while queue:
            # on first iteration, current_word = beginWord, level = 1
            current_word, level = queue.popleft() 
            for i in range(L):
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]
                for word in combinations[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, level+1))
        return 0
            

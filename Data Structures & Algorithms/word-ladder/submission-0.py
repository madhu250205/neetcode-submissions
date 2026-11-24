from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
            
        # Step 1: Pre-process the wordList to create wildcard pattern mappings (adjacency list)
        # e.g., "hit" -> "*it", "h*t", "hi*"
        allComboDict = defaultdict(list)
        wordList.append(beginWord)
        
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                allComboDict[pattern].append(word)
                
        # Step 2: BFS initialization
        queue = deque([(beginWord, 1)])
        visit = {beginWord}
        
        while queue:
            current_word, level = queue.popleft()
            
            if current_word == endWord:
                return level
                
            for j in range(len(current_word)):
                pattern = current_word[:j] + "*" + current_word[j+1:]
                
                for neighbor in allComboDict[pattern]:
                    if neighbor not in visit:
                        visit.add(neighbor)
                        queue.append((neighbor, level + 1))
                        
                # Clear the pattern list so we don't re-traverse old transformations
                allComboDict[pattern] = []
                
        return 0
        
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        """Initializes the WordDictionary object."""
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """Adds word to the data structure."""
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        """Returns true if word is in the data structure, where '.' matches any letter."""
        def dfs(j, root):
            curr = root
            
            for i in range(j, len(word)):
                char = word[i]
                
                if char == '.':
                    # If it's a wildcard dot, try all possible child paths recursively
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]
            
            return curr.endOfWord

        return dfs(0, self.root)
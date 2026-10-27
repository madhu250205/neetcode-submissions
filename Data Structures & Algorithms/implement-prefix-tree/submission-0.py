class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        """PrefixTree() initializes the prefix tree object."""
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Inserts the string word into the prefix tree."""
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        """Returns true if the string word is in the prefix tree (i.e., was inserted before), and false otherwise."""
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        """Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise."""
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True
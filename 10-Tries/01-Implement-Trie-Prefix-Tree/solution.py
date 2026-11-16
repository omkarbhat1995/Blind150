class TrieNode:
    def __init__(self):
        """
        Helper class representing a single character node in the Trie.
        """
        self.children = {}
        self.is_end_of_word = False

class PrefixTree:
    def __init__(self):
        """
        Initializes the prefix tree object.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts the string word into the prefix tree.
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        
        # Mark the final node as the end of a valid inserted word
        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        Returns true if the string word is in the prefix tree.
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
            
        # Must be explicitly marked as the end of a word, not just a prefix
        return curr.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns true if there is any inserted string that starts with the given prefix.
        """
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
            
        # As long as we successfully traversed the prefix, it exists
        return True
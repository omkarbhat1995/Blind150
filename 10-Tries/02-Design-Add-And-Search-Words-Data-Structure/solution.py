class TrieNode:
    def __init__(self):
        """
        Represents a single node in the WordDictionary Trie.
        Stores children in a dictionary for O(1) character lookups.
        """
        self.children = {}
        self.is_end_of_word = False


class WordDictionary:
    def __init__(self):
        """
        Initializes the WordDictionary object with an empty root node.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        Returns true if there is any string in the data structure that matches word.
        Uses Depth-First Search (DFS) to backtrack when a wildcard '.' is encountered.
        """
        def dfs(index: int, root: TrieNode) -> bool:
            curr = root
            
            for i in range(index, len(word)):
                char = word[i]
                
                # If we hit a wildcard, we must recursively check all existing child branches
                if char == '.':
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    # Standard Trie traversal
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]
                    
            return curr.is_end_of_word

        return dfs(0, self.root)
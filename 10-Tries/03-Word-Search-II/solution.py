from typing import List

class TrieNode:
    def __init__(self):
        """
        Represents a single character node in the Trie.
        Tracks children nodes and stores the complete word at the leaf.
        """
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Finds all words from a list that exist on a 2D board.
        Uses a Trie to optimize prefix matching and Backtracking/DFS to traverse the board.
        """
        # Step 1: Build the Trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word  # Store the full word at the end node
        
        ROWS, COLS = len(board), len(board[0])
        res = []
        visited = set()

        def dfs(r: int, c: int, node: TrieNode):
            # Base cases: out of bounds, already visited, or no matching prefix in Trie
            if (r < 0 or c < 0 or 
                r == ROWS or c == COLS or 
                (r, c) in visited or 
                board[r][c] not in node.children):
                return
            
            visited.add((r, c))
            node = node.children[board[r][c]]
            
            # If we reached a valid word, add it and remove it from Trie to prevent duplicates
            if node.word:
                res.append(node.word)
                node.word = None
                
            # Explore all 4 adjacent directions
            dfs(r - 1, c, node)
            dfs(r + 1, c, node)
            dfs(r, c - 1, node)
            dfs(r, c + 1, node)
            
            # Backtrack
            visited.remove((r, c))
            
            # Optimization: if the current Trie node has no children left, prune it
            if not node.children:
                del node

        # Step 2: Run DFS starting from every cell in the board
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)
                
        return res
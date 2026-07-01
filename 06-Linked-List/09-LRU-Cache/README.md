# LRU Cache

**Difficulty:** Medium
**Topics:** Hash Table, Linked List, Design, Doubly-Linked List

## Problem Description

Implement the Least Recently Used (LRU) cache class `LRUCache`. The class should support the following operations:

* `LRUCache(int capacity)`: Initialize the LRU cache with positive size `capacity`.
* `int get(int key)`: Return the value of the `key` if the key exists, otherwise return `-1`.
* `void put(int key, int value)`: Update the value of the `key` if the `key` exists. Otherwise, add the `key-value` pair to the cache. If the number of keys exceeds the `capacity` from this operation, evict the least recently used key.

**Constraint:** The functions `get` and `put` must each run in $O(1)$ average time complexity.

## Approach: Hash Map + Doubly Linked List

To achieve $O(1)$ operations, we must combine two data structures:
1.  **Hash Map:** Maps a key to its corresponding Node in the linked list, giving us $O(1)$ lookups.
2.  **Doubly Linked List:** Allows us to insert or remove a node in $O(1)$ time once we have its reference from the hash map. 

We maintain two dummy nodes, `left` (representing the Least Recently Used boundary) and `right` (representing the Most Recently Used boundary). 
* Every time a node is created or accessed via `get`, it is extracted from its current position and inserted right before the `right` dummy node.
* When capacity is exceeded, we evict the node immediately following the `left` dummy node, as it is strictly the least recently used.

## Complexity
- **Time Complexity:** $O(1)$ for both `get` and `put`. We only perform direct dictionary lookups and constant-time pointer reassignments.
- **Space Complexity:** $O(capacity)$ where `capacity` is the maximum number of items allowed in the cache. This space is used by the Hash Map and the Doubly Linked List nodes.
# 🚀 NeetCode 150 - Professional Python Portfolio
Welcome to my NeetCode 150 showcase repository! This repository contains clean, optimized Python solutions and robust, enterprise-grade test suites for the top 150 algorithmic patterns.

Instead of a messy collection of unorganized scripts, this project is structured to demonstrate professional software engineering standards, Test-Driven Development (TDD), and meticulous QA practices.

  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />


## 📂 Repository Structure
The repository mirrors the official NeetCode roadmap, categorized by algorithmic patterns to showcase a deep understanding of core computer science fundamentals:
```
├── 01-Arrays-and-Hashing/
│   ├── 01-Contains-Duplicate/
│   │   ├── README.md
│   │   ├── solution.py
│   │   └── test_solution.py
│   └── ...
├── 02-Two-Pointers/
├── 03-Sliding-Window/
├── 04-Stack/
├── 05-Binary-Search/
├── 06-Linked-List/
├── 07-Trees/
├── 08-Heap-Priority-Queue/
├── 17-Math-and-Geometry/
└── 18-Bit-Manipulation/
```
## 🛠️ Engineering Standards

Every single problem folder in this repository is treated as an independent module complete with:
1. **Production-Ready Code (`solution.py`)**: Written in Python with full type hints (`typing` module) for static analysis, optimal time and space complexity, and clean docstrings.
2. **Comprehensive Unit Tests (`test_solution.py`)**: Leverages `pytest` with parameterized test suites containing **15+ distinct test cases** per problem. This covers standard examples, boundary limits, negative constraints, and complex logical edge cases.
3. **Dedicated Documentation (`README.md`)**: Contains problem descriptions, complexity analysis, approach breakdowns, and instructions for running local checks.


## 🚀 How to Run the Test Suite
To ensure code integrity and run the test framework locally, follow these steps:

1. Clone the repository and navigate to the root directory:
```bash
git clone https://github.com/YOUR_USERNAME/neetcode-150-python.git
cd neetcode-150-python
```
2. Set up a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```
3. Install dependencies (pytest):
```bash
pip install pytest
```
4. Run all tests recursively with verbose output:
```bash
pytest -v
```
(Or run tests for a specific folder/problem using: pytest 01-Arrays-and-Hashing/01-Contains-Duplicate/test_solution.py -v)


---

## 📈 Progress Dashboard

**Overall Completion:** `82 / 150`
*(Click on any category to expand and see the specific problems, solutions, and complexities!)*

<details open>
<summary><b>1. Arrays & Hashing [9 / 9]</b></summary>
<br>

| Status | Problem | Language | Time | Space |
| :---: | :--- | :---: | :---: | :---: |
| ✅ | [Contains Duplicate](./01-Arrays-and-Hashing/01-Contains-Duplicate) | Python | $O(n)$ | $O(n)$ |
| ✅ | [Valid Anagram](./01-Arrays-and-Hashing/02-Valid-Anagram) | Python | $O(n + m)$ | $O(1)$ |
| ✅ | [Two Sum](./01-Arrays-and-Hashing/03-Two-Sum) | Python  | $O(n)$ | $O(n)$ |
| ✅ | [Group Anagrams](./01-Arrays-and-Hashing/04-Group-Anagrams) | Python  | $O(m*n)$ | $O(m*n)$ |
| ✅ | [Top-K Frequent Elements](./01-Arrays-and-Hashing/05-Top-K-Frequent-Elements) | Python  | $O(n)$ | $O(n)$ |
| ✅ | [Encode Decode Strings](./01-Arrays-and-Hashing/06-Encode-Decode-Strings) | Python  | $O(n)$ | $O(n)$ |
| ✅ | [Product of Array Except Self](./01-Arrays-and-Hashing/07-Product-of-Array-Except-Self) | Python  |$O(n)$ | $O(1)$ |
| ✅ | [Valid Sudoku](./01-Arrays-and-Hashing/08-Valid-Sudoku) | Python  | $O(1)$ | $O(1)$ |
| ✅ | [Longest Consecutive Sequence](./01-Arrays-and-Hashing/09-Longest-Consecutive-Sequence) | Python  | $O(n)$ | $O(n)$ |

</details>

<details>
<summary><b>2. Two Pointers [5 / 5]</b></summary>
<br>

| Status | Problem | Language | Time | Space |
| :---: | :--- | :---: | :---: | :---: |
| ✅ | [Valid Palindrome](./02-Two-Pointers/01-Valid-Palindrome) | Python | $O(n)$ | $O(1)$ |
| ✅ | [Two Sum II](./02-Two-Pointers/02-Two-Sum-II-Input-Array-Is-Sorted) | Python  | $O(n)$ | $O(1)$ |
| ✅ | [3Sum](./02-Two-Pointers/03-3Sum) | Python  | $O(n^2)$ | $O(1)$ |
| ✅ | [Container-with-Most-Water](./02-Two-Pointers/04-Container-with-Most-Water) | Python  | $O(n)$ | $O(1)$ |
| ✅ | [Trapping-Rain-Water](./02-Two-Pointers/05-Trapping-Rain-Water) | Python  | $O(n)$ | $O(1)$ |
</details>

<details>
<summary><b>3. Sliding Window [6 / 6]</b></summary>
<br>

| Status | Problem | Language | Time | Space |
| :---: | :--- | :---: | :---: | :---: |
| ✅ | [Best Time to Buy and Sell Stock](./03-Sliding-Window/01-Best-Time-to-Buy-and-Sell-Stock) | Python | $O(n)$ | $O(1)$ |
| ✅ | [Longest Substring Without Repeating Characters](./03-Sliding-Window/02-Longest-Substring-Without-Repeating-Characters/) | Python | $O(n)$ | $O(m)$ |
| ✅ | [Longest Repeating Character Replacement](./03-Sliding-Window//03-Longest-Repeating-Character-Replacement/) |  Python | $O(n)$ | $O(1)$ |
| ✅ | [Permutation in String](./03-Sliding-Window//04-Permutation-in-String/) | Python | $O(l_1 + l_2)$ | $O(1)$ |
| ✅ | [Minimum Window Substring](./03-Sliding-Window//05-Minimum-Window-Substring/) | Python | $O(|s| + |t|)$ | $O(1)$ |
| ✅ | [Sliding Window Maximum](./03-Sliding-Window//06-Sliding-Window-Maximum/) | Python | $O(n)$ | $O(k)$ |
</details>

<details>
<summary><b>4. Stack [7 / 7]</b></summary>
<br>

| Status | Problem | Language | Time | Space |
| :---: | :--- | :---: | :---: | :---: |
| ✅ | [Valid Parentheses](./04-Stack/01-Valid-Parentheses) | Python | $O(n)$ | $O(n)$ |
| ✅ | [Min Stack](./04-Stack/02-Min-Stack/) | Python | $O(1)$ | $O(n)$ |
| ✅ | [Evaluate Reverse Polish Notation](./04-Stack/03-Evaluate-Reverse-Polish-Notation/) | Python | $O(n)$ | $O(n)$ |
| ✅ | [Daily Temperatures](./04-Stack/04-Daily-Temperatures/) | Python | $O(n)$ | $O(n)$ |
| ✅ | [Car Fleet](./04-Stack/05-Car-Fleet/) | Python | $O(n \log(n))$ | $O(n)$ |
| ✅ | [Largest Rectangle In Histogram](./04-Stack/06-Largest-Rectangle-In-Histogram/) | Python | $O(n)$ | $O(n)$ |
</details>

<details>
<summary><b>5. Binary Search [7 / 7]</b></summary>
<br>

| Status | Problem | Language | Time | Space |
| :---: | :--- | :---: | :---: | :---: |
| ✅ | [Binary Search](./05-Binary-Search/01-Binary-Search) | Python | $O(\log n)$ | $O(1)$ |
| ✅ | [Search a 2D Matrix](./05-Binary-Search/02-Search-a-2D-Matrix/) | Python | $O(\log(m*n))$ | $O(1)$ |
| ✅ | [Koko Eating Bananas](./05-Binary-Search/03-Koko-Eating-Bananas/) | Python | $O(n\log(m))$ | $O(n)$ |
| ✅ | [Find Minimum in Rotated Sorted Array](./05-Binary-Search/04-Find-Minimum-in-Rotated-Sorted-Array/) | Python | $O(\log(n))$ | $O(1)$ |
| ✅ | [Search in Rotated Sorted Array](./05-Binary-Search/05-Search-in-Rotated-Sorted-Array/) | Python | $O(\log(n))$ | $O(1)$ |
| ✅ | [Time Based Key Value Store](./05-Binary-Search/06-Time-Based-Key-Value-Store/) | Python | $O(1) and $O(\log(n))$ | $O(m)$ |
| ✅ | [Median of Two Sorted Arrays](./05-Binary-Search/07-Median-of-Two-Sorted-Arrays/) | Python | $O(\log(\min(m,n)))$ | $O(1)$ |
</details>

<details>
<summary><b>6. Linked List [11 / 11]</b></summary>
<br>

| Status | Problem | Language | Time | Space |
| :---: | :--- | :---: | :---: | :---: |
| ✅ | [Reverse Linked List](./06-Linked-List/01-Reverse-Linked-List) | Python | $O(n)$ | $O(1)$ |
| ✅ | [Merge Two Sorted Lists](./06-Linked-List/02-Merge-Two-Sorted-Linked-Lists/) | Python | $O(n+m)$ | $O(1)$ |
| ✅ | [Linked List Cycle Detection](./06-Linked-List/03-Linked-List-Cycle-Detection) | Python | $O(n)$ | $O(1)$ |
| ✅ | [Reorder Linked List](./06-Linked-List/04-Reorder-Linked-List/) | Python | $O(n)$ | $O(1)$ |
| ✅ | [Remove Nth Node From End of List](./06-Linked-List/05-Remove-Nth-Node-From-End-of-List/) | Python | $O(sz)$ | $O(1)$ |
| ✅ | [Copy Linked List with Random Pointer](./06-Linked-List/06-Copy-Linked-List-with-Random-Pointer/) | Python | $O(n)$ | $O(n)$ |
| ✅ | [Add Two Numbers](./06-Linked-List/07-Add-Two-Numbers/) | Python | $O(\max(m,n))$ | $O(\max(m,n))$ |
| ✅ | [Find the Duplicate Number](./06-Linked-List/08-Find-the-Duplicate-Number/) | Python | $O(n)$ | $O(1)$ |
| ✅ | [LRU Cache](./06-Linked-List/09-LRU-Cache/) | Python | $O(1)$ | $O(capacity)$ |
| ✅ | [Merge K-Sorted Linked Lists](./06-Linked-List/10-Merge-K-Sorted-Linked-Lists/) | Python | $O(n\log(k))$ | $O(k)$ |
| ✅ | [Reverse Nodes in K-Group](./06-Linked-List/11-Reverse-Nodes-in-K-Group/) | Python | $O(n)$ | $O(1)$ |
</details>

<details>
<summary><b>7. Trees [15 / 15]</b></summary>
<br>

| Status | Problem | Language | Time | Space |
| :---: | :--- | :---: | :---: | :---: |
| ✅ | [Invert Binary Tree](./07-Trees/01-Invert-Binary-Tree) | Python | $O(n)$ | $O(n)$ |
| ✅ | [Maximum Depth of Binary Tree](./07-Trees/02-Maximum-Depth-of-Binary-Tree/) | Python | $O(n)$ | $O(h)$ |
| ✅ | [Diameter-of-Binary-Tree](./07-Trees/03-Diameter-of-Binary-Tree/) | Python | $O(n)$ | $O(h)$ |
| ✅ | [Balanced-Binary-Tree](./07-Trees/04-Balanced-Binary-Tree/) | Python | $O(n)$ | $O(h)$ |
| ✅ | [Same-Tree](./07-Trees/05-Same-Tree/) | Python | $O(n)$ | $O(h)$ |
| ✅ | [Subtree-of-Another-Tree](./07-Trees/06-Subtree-of-Another-Tree/) | Python | $O(m*n)$ | $O(h)$ |
| ✅ | [Lowest-Common-Ancestor-of-a-Binary-Search-Tree](./07-Trees/07-Lowest-Common-Ancestor-of-a-Binary-Search-Tree/) | Python | $O(h)$ | $O(h)$ |
| ✅ | [Binary-Tree-Level-Order-Traversal](./07-Trees/08-Binary-Tree-Level-Order-Traversal/) | Python | $O(n)$ | $O(w)$ |
| ✅ | [Binary-Tree-Right-Side-View](./07-Trees/09-Binary-Tree-Right-Side-View/) | Python | $O(n)$ | $O(w)$ |
| ✅ | [Count-Good-Nodes-In-Binary-Tree](./07-Trees/10-Count-Good-Nodes-In-Binary-Tree/) | Python | $O(n)$ | $O(h)$ |
| ✅ | [Validate-Binary-Search-Tree](./07-Trees/11-Validate-Binary-Search-Tree/) | Python | $O(n)$ | $O(h)$ |
| ✅ | [Kth-Smallest-Element-In-a-Bst](./07-Trees/12-Kth-Smallest-Element-In-a-Bst/) | Python | $O(h+k)$ | $O(h)$ |
| ✅ | [Construct-Binary-Tree-From-Preorder-And-Inorder-Traversal](./07-Trees/13-Construct-Binary-Tree-From-Preorder-And-Inorder-Traversal/) | Python | $O(n)$ | $O(n)$ |
| ✅ | [Binary-Tree-Maximum-Path-Sum](./07-Trees/14-Binary-Tree-Maximum-Path-Sum/) | Python | $O(n)$ | $O(h)$ |
| ✅ | [Serialize-And-Deserialize-Binary-Tree](./07-Trees/15-Serialize-And-Deserialize-Binary-Tree/) | Python | $O(n)$ | $O(n)$ |
</details>

<details>
<summary><b>8. Heap Priority Queue [7 / 7]</b></summary>
<br>

| Status | Problem | Language | Time | Space |
| :---: | :--- | :---: | :---: | :---: |
| ✅ | [Kth-Largest Element in a Stream](./08-Heap-Priority-Queue/01-Kth-Largest-Element_in_a_Stream/) | Python | $O(n\log(k))$ | $O(k)$ |
| ✅ | [Last Stone Weight](./08-Heap-Priority-Queue/02-Last-Stone-Weight/) | Python | $O(n\log(n))$ | $O(n)$ or $O(1)$ |
| ✅ | [K-Closest Points to Origin](/08-Heap-Priority-Queue/03-K-Closest-Points-to-Origin/) | Python | $O(n\log(k))$ | $O(k)$ |
| ✅ | [Kth-Largest Element In An Array](/08-Heap-Priority-Queue/04-Kth-Largest-Element-In-An-Array/) | Python | $O(n\log(n))$ and $O(\log(k))$ | $O(n)$ |
| ✅ | [Task Scheduler](/08-Heap-Priority-Queue/05-Task-Scheduler/) | Python | $O(n)$ | $O(1)$ |
| ✅ | [Design Twitter](/08-Heap-Priority-Queue/06-Design-Twitter/) | Python | $O(f)$ | $O(T+(U*F))$ |
| ✅ | [Find Median From Data Stream](/08-Heap-Priority-Queue/07-Find-Median-From-Data-Stream/) | Python | $O(\log(n))$ | $O(n)$ |

</details>

<details>
<summary><b>9. Backtracking [0 / 10]</b></summary>
<br>

| Status | Problem | Language | Time | Space |
| :---: | :--- | :---: | :---: | :---: |
| ⬜️ | [Subsets](/09-Backtracking/01-Subsets/) | Python | | |
| ⬜️ | [Combination Sum](/09-Backtracking/02-Combination-Sum/) | Python | | |
| ⬜️ | [Combination Sum II](/09-Backtracking/03-Combination-Sum-II/) | Python | | |
| ⬜️ | [Permutations](/09-Backtracking/04-Permutations/) | Python | | |
| ⬜️ | [Generate Parentheses](/09-Backtracking/06-Generate-Parentheses/) | Python | | |
| ⬜️ | [Word Search](/09-Backtracking/07-Word-Search/) | Python | | |
| ⬜️ | [Palindrome Partitioning](/09-Backtracking/08-Palindrome-Partitioning/) | Python | | |
| ⬜️ | [Letter Combination of a Phone Number](/09-Backtracking/09-Letter-Combination-of-a-Phone-Number/) | Python | | |
| ⬜️ | [N-Queens](/09-Backtracking/10-N-Queens/) | Python | | |
| ⬜️ | [](/09-Backtracking) | Python | | |
</details>


<details>
<summary><b>10. Tries [0 / 3]</b></summary>
<br>

| Status | Problem | Language | Time | Space |
| :---: | :--- | :---: | :---: | :---: |
| ⬜️ | [Implement Trie Prefix Tree](/10-Tries/01-Implement-Trie-Prefix-Tree/) | Python | | |
| ⬜️ | [Design Add And Search Words Data Structure](/10-Tries/02-Design-Add-And-Search-Words-Data-Structure/) | Python | | |
| ⬜️ | [Word Search II](/10-Tries/03-Word-Search-II/) | Python | | |
</details>



<details>
<summary><b>11. Graphs [0 / 13]</b></summary>
<br>

| Status | Problem | Language | Time | Space |
| :---: | :--- | :---: | :---: | :---: |
| ⬜️ | [Number of Islands](/11-Graphs/01-Number-of-Islands/) | Python | | |
| ⬜️ | [Max Area of Island](/11-Graphs/02-Max-Area-of-Island/) | Python | | |
| ⬜️ | [Clone Graph](/11-Graphs/03-Clone-Graph/) | Python | | |
| ⬜️ | [Walls And Gates](/11-Graphs/04-Walls-And-Gates/) | Python | | |
| ⬜️ | [Rotting Oranges](/11-Graphs/05-Rotting-Oranges/) | Python | | |
| ⬜️ | [Pacific Atlantic Water Flow](/11-Graphs/06-Pacific-Atlantic-Water-Flow/) | Python | | |
| ⬜️ | [Surrounded Regions](/11-Graphs/07-Surrounded-Regions/) | Python | | |
| ⬜️ | [Course Schedule](/11-Graphs/08-Course-Schedule/) | Python | | |
| ⬜️ | [Course Schedule II](/11-Graphs/09-Course-Schedule-II/) | Python | | |
| ⬜️ | [Graph Valid Tree](/11-Graphs/10-Graph-Valid-Tree/) | Python | | |
| ⬜️ | [Number of Connected Components In An Undirected Graph](/11-Graphs/11-Number-of-Connected-Components-In-An-Undirected-Graph/) | Python | | |
| ⬜️ | [Redundant Connection](/11-Graphs/12-Redundant-Connection/) | Python | | |
| ⬜️ | [Word Ladder](/11-Graphs/13-Word-Ladder/) | Python | | |
</details>

<details>
<summary><b>12. Advanced Graphs [0 / 6]</b></summary>
<br>

| Status | Problem | Language | Time | Space |
| :---: | :--- | :---: | :---: | :---: |
| ⬜️ | [Network Delay Time](/12-Adv-Graphs/01-Network-Delay-Time/) | Python | | |
| ⬜️ | [Reconstruct Itinerary](/12-Adv-Graphs/02-Reconstruct-Itinerary/) | Python | | |
| ⬜️ | [Min Cost to Connect All Points](/12-Adv-Graphs/03-Min-Cost-to-Connect-All-Points/) | Python | | |
| ⬜️ | [Swim In Rising Water](/12-Adv-Graphs/04-Swim-In-Rising-Water/) | Python | | |
| ⬜️ | [Alien Dictionary](/12-Adv-Graphs/05-Alien-Dictionary/) | Python | | |
| ⬜️ | [Cheapest Flights Within K-Stops](/12-Adv-Graphs/06-Cheapest-Flights-Within-K-Stops/) | Python | | |
</details>


<details>
<summary><b>13. 1-D Dynamic Programming [0 / 12]</b></summary>
<br>

| Status | Problem | Language | Time | Space |
| :---: | :--- | :---: | :---: | :---: |
| ⬜️ | [Climbing Stairs](/13-1-D-Dynamic-Programming/01-Climbing-Stairs/) | Python | | |
| ⬜️ | [Min Cost Climbing Stairs](/13-1-D-Dynamic-Programming/02-Min-Cost-Climbing-Stairs/) | Python | | |
| ⬜️ | [House Robber](/13-1-D-Dynamic-Programming/03-House-Robber/) | Python | | |
| ⬜️ | [House Robber II](/13-1-D-Dynamic-Programming/04-House-Robber-II/) | Python | | |
| ⬜️ | [Longest Palindromic Substring](/13-1-D-Dynamic-Programming/05-Longest-Palindromic-Substring/) | Python | | |
| ⬜️ | [Palindromic Substrings](/13-1-D-Dynamic-Programming/06-Palindromic-Substrings/) | Python | | |
| ⬜️ | [Decode Ways](/13-1-D-Dynamic-Programming/07-Decode-Ways/) | Python | | |
| ⬜️ | [Coin Change](/13-1-D-Dynamic-Programming/08-Coin-Change/) | Python | | |
| ⬜️ | [Maximum Product Subarray](/13-1-D-Dynamic-Programming/09-Maximum-Product-Subarray/) | Python | | |
| ⬜️ | [Word Break](/13-1-D-Dynamic-Programming/10-Word-Break/) | Python | | |
| ⬜️ | [Longest Increasing Subsequence](/13-1-D-Dynamic-Programming/11-Longest-Increasing-Subsequence/) | Python | | |
| ⬜️ | [Patition Equal Subset Sum](/13-1-D-Dynamic-Programming/12-Patition-Equal-Subset-Sum/) | Python | | |

</details>



<details>
<summary><b>14. 2-D Dynamic Programming [0 / 11]</b></summary>
<br>

| Status | Problem | Language | Time | Space |
| :---: | :--- | :---: | :---: | :---: |
| ⬜️ | [Unique Paths](/14-2-D-Dynamic-Programming/01-Unique-Paths/) | Python | | |
| ⬜️ | [Longest Common Subsequence](/14-2-D-Dynamic-Programming/02-Longest-Common-Subsequence/) | Python | | |
| ⬜️ | [Best Time to Buy And Sell Stock With Cooldown](/14-2-D-Dynamic-Programming/03-Best-Time-to-Buy-And-Sell-Stock-With-Cooldown/) | Python | | |
| ⬜️ | [Coin Change II](/14-2-D-Dynamic-Programming/04-Coin-Change-II/) | Python | | |
| ⬜️ | [Target Sum](/14-2-D-Dynamic-Programming/05-Target-Sum/) | Python | | |
| ⬜️ | [Interleaving String](/14-2-D-Dynamic-Programming/06-Interleaving-String/) | Python | | |
| ⬜️ | [Longest Increasing Path In a Matrix](/14-2-D-Dynamic-Programming/07-Longest-Increasing-Path-In-a-Matrix/) | Python | | |
| ⬜️ | [Distinct Subsequences](/14-2-D-Dynamic-Programming/08-Distinct-Subsequences/) | Python | | |
| ⬜️ | [Edit Distance](/14-2-D-Dynamic-Programming/09-Edit-Distance/) | Python | | |
| ⬜️ | [Burst Balloons](/14-2-D-Dynamic-Programming/10-Burst-Balloons/) | Python | | |
| ⬜️ | [Regular Expression Matching](/14-2-D-Dynamic-Programming/11-Regular-Expression-Matching/) | Python | | |
</details>

<details>
<summary><b>15. Greedy [0 / 8]</b></summary>
<br>

| Status | Problem | Language | Time | Space |
| :---: | :--- | :---: | :---: | :---: |
| ⬜️ | [Maximum Subarray](/15-Greedy/01-Maximum-Subarray/) | Python | | |
| ⬜️ | [Jump Game/](/15-Greedy/02-Jump-Game/) | Python | | |
| ⬜️ | [Jump Game II/](/15-Greedy/03-Jump-Game-II/) | Python | | |
| ⬜️ | [Gas Station](/15-Greedy/04-Gas-Station/) | Python | | |
| ⬜️ | [Hand of Straights](/15-Greedy/05-Hand-of-Straights/) | Python | | |
| ⬜️ | [Merge Triplets to Form Target Triplet](/15-Greedy/06-Merge-Triplets-to-Form-Target-Triplet/) | Python | | |
| ⬜️ | [Partition Labels](/15-Greedy/07-Partition-Labels/) | Python | | |
| ⬜️ | [Valid Parenthesis String](/15-Greedy/08-Valid-Parenthesis-String/) | Python | | |
</details>


<details>
<summary><b>16. Intervals [0 / 6]</b></summary>
<br>

| Status | Problem | Language | Time | Space |
| :---: | :--- | :---: | :---: | :---: |
| ⬜️ | [Insert Interval](/16-Intervals/01-Insert-Interval/) | Python | | |
| ⬜️ | [Merge Intervals](/16-Intervals/02-Merge-Intervals/) | Python | | |
| ⬜️ | [Non-Overlapping Intervals](/16-Intervals/03-Non-Overlapping-Intervals/) | Python | | |
| ⬜️ | [Meeting Rooms ](/16-Intervals/04-Meeting-Rooms/) | Python | | |
| ⬜️ | [Meeting Rooms II](/16-Intervals/05-Meeting-Rooms-II/) | Python | | |
| ⬜️ | [Minimum Interval to Include Each Query](/16-Intervals/06-Minimum-Interval-to-Include-Each-Query/) | Python | | |
</details>


<details>
<summary><b>17. Math and Geometry [8 / 8]</b></summary>
<br>

| Status | Problem | Language | Time | Space |
| :---: | :--- | :---: | :---: | :---: |
| ✅ | [Rotate Image](./17-Math-and-Geometry/01-Rotate-Image/) | Python | | |
| ✅ | [Spiral Matrix](./17-Math-and-Geometry/02-Spiral-Matrix/) | Python | | |
| ✅ | [Set Matrix Zeroes](./17-Math-and-Geometry/03-Set-Matrix-Zeroes/) | Python | | |
| ✅ | [Happy Number](./17-Math-and-Geometry/04-Happy-Number/) | Python | | |
| ✅ | [PLus One](./17-Math-and-Geometry/05-PLus-One/) | Python | | |
| ✅ | [Pow](./17-Math-and-Geometry/06-Pow/) | Python | | |
| ✅ | [Multiply Strings](./17-Math-and-Geometry/07-Multiply-Strings/) | Python | | |
| ✅ | [Detect Squares](./17-Math-and-Geometry/08-Detect-Squares/) | Python | | |
</details>



<details>
<summary><b>18. Bit-Manipulation [7 / 7]</b></summary>
<br>

| Status | Problem | Language | Time | Space |
| :---: | :--- | :---: | :---: | :---: |
| ✅ | [Single Number](./18-Bit-Manipulation/01-Single-Number/) | Python | | |
| ✅ | [Number of 1-Bits](./18-Bit-Manipulation/02-Number-of-1-Bits/) | Python | | |
| ✅ | [Counting Bits](./18-Bit-Manipulation/03-Counting-Bits/) | Python | | |
| ✅ | [Reverse Bits](./18-Bit-Manipulation/04-Reverse-Bits/) | Python | | |
| ✅ | [Missing Number](./18-Bit-Manipulation/05-Missing-Number/) | Python | | |
| ✅ | [Sum of Two Integers](./18-Bit-Manipulation/06-Sum-of-Two-Integers/) | Python | | |
| ✅ | [Reverse Integer](./18-Bit-Manipulation/07-Reverse-Integer/) | Python | | |
</details>


<!--
## 📈 Progress Tracker
| Status | Category         | Problem                         | Language |
|---------|------------------|---------------------------------|----------|
| ✅      | Arrays & Hashing   | Contains Duplicate              | Python   |
| ✅      |                    | Valid Anagram                   | Python   |
| ✅      | Two Pointers       | Valid Palindrome                | Python   |
| ✅      | Sliding Window     | Best Time to Buy and Sell Stock | Python   |
| ✅      | Stack              | Valid Parentheses               | Python   | 
| ✅      | Binary Search      | Binary Search                   | Python   | 
| ✅      | Linked List        | Reverse Linked List             | Python   |
| ✅      | Trees              | Invert Binary Tree              | Python   | 
| ✅      | Heap Priority Queue| Invert Binary Tree              | Python   | 
| ✅      | Math-and-Geometry  | Invert Binary Tree              | Python   | 
| ✅      | Bit-Manipulation   | Invert Binary Tree              | Python   | 

(...and continually expanding through the complete NeetCode roadmap!)
-->
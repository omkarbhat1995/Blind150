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

**Overall Completion:** `11 / 150`
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
| ✅ | [Two Sum II](./02-Two-Pointers/02-Two-Sum-II-Input-Array-Is-Sorted) | | | |
| ✅ | [3Sum](./02-Two-Pointers/03-3Sum) | | | |
| ✅ | [Container-with-Most-Water](./02-Two-Pointers/04-Container-with-Most-Water) | | | |
| ✅ | [Trapping-Rain-Water](./02-Two-Pointers/05-Trapping-Rain-Water) | | | |
</details>

<details>
<summary><b>3. Sliding Window [6 / 6]</b></summary>
<br>

| Status | Problem | Language | Time | Space |
| :---: | :--- | :---: | :---: | :---: |
| ✅ | [Best Time to Buy and Sell Stock](./03-Sliding-Window/01-Best-Time-to-Buy-and-Sell-Stock) | Python | $O(n)$ | $O(1)$ |
| ✅ | [Longest Substring Without Repeating Characters](./03-Sliding-Window/02-Longest-Substring-Without-Repeating-Characters/) | | | |
| ✅ | [Longest Repeating Character Replacement](./03-Sliding-Window//03-Longest-Repeating-Character-Replacement/) | | | |
| ✅ | [Permutation in String](./03-Sliding-Window//04-Permutation-in-String/) | | | |
| ✅ | [Minimum Window Substring](./03-Sliding-Window//05-Minimum-Window-Substring/) | | | |
| ✅ | [Sliding Window Maximum](./03-Sliding-Window//06-Sliding-Window-Maximum/) | | | |
</details>

<details>
<summary><b>4. Stack [7 / 7]</b></summary>
<br>

| Status | Problem | Language | Time | Space |
| :---: | :--- | :---: | :---: | :---: |
| ✅ | [Valid Parentheses](./04-Stack/01-Valid-Parentheses) | Python | $O(n)$ | $O(n)$ |
| ✅ | [Min Stack](./04-Stack/02-Min-Stack/) | | | |
| ✅ | [Evaluate Reverse Polish Notation](./04-Stack/03-Evaluate-Reverse-Polish-Notation/) | | | |
| ✅ | [Daily Temperatures](./04-Stack/04-Daily-Temperatures/) | | | |
| ✅ | [Car Fleet](./04-Stack/05-Car-Fleet/) | | | |
| ✅ | [Largest Rectangle In Histogram](./04-Stack/06-Largest-Rectangle-In-Histogram/) | | | |
</details>

<details>
<summary><b>5. Binary Search [7 / 7]</b></summary>
<br>

| Status | Problem | Language | Time | Space |
| :---: | :--- | :---: | :---: | :---: |
| ✅ | [Binary Search](./05-Binary-Search/01-Binary-Search) | Python | $O(\log n)$ | $O(1)$ |
| ✅ | [Search a 2D Matrix](./05-Binary-Search/02-Search-a-2D-Matrix/) | | | |
| ✅ | [Koko Eating Bananas](./05-Binary-Search/03-Koko-Eating-Bananas/) | | | |
| ✅ | [Find Minimum in Rotated Sorted Array](./05-Binary-Search/04-Find-Minimum-in-Rotated-Sorted-Array/) | | | |
| ✅ | [Search in Rotated Sorted Array](./05-Binary-Search/05-Search-in-Rotated-Sorted-Array/) | | | |
| ✅ | [Time Based Key Value Store](./05-Binary-Search/06-Time-Based-Key-Value-Store/) | | | |
| ✅ | [Median of Two Sorted Arrays](./05-Binary-Search/07-Median-of-Two-Sorted-Arrays/) | | | |
</details>

<details>
<summary><b>6. Linked List [11 / 11]</b></summary>
<br>

| Status | Problem | Language | Time | Space |
| :---: | :--- | :---: | :---: | :---: |
| ✅ | [Reverse Linked List](./06-Linked-List/01-Reverse-Linked-List) | Python | $O(n)$ | $O(1)$ |
| ✅ | [Merge Two Sorted Lists](./06-Linked-List/02-Merge-Two-Sorted-Linked-Lists/) | | | |
| ✅ | [](./06-Linked-List/03-Linked-List-Cycle-Detection) | | | |
| ✅ | [](./06-Linked-List/04-Reorder-Linked-List/) | | | |
| ✅ | [](./06-Linked-List/05-Remove-Nth-Node-From-End-of-List/) | | | |
| ✅ | [](./06-Linked-List/06-Copy-Linked-List-with-Random-Pointer/) | | | |
| ✅ | [](./06-Linked-List/07-Add-Two-Numbers/) | | | |
| ✅ | [](./06-Linked-List/08-Find-the-Duplicate-Number/) | | | |
| ✅ | [](./06-Linked-List/09-LRU-Cache/) | | | |
| ✅ | [](./06-Linked-List/10-Merge-K-Sorted-Linked-Lists/) | | | |
| ✅ | [](./06-Linked-List/11-Reverse-Nodes-in-K-Group/) | | | |
</details>

<details>
<summary><b>7. Trees [15 / 15]</b></summary>
<br>

| Status | Problem | Language | Time | Space |
| :---: | :--- | :---: | :---: | :---: |
| ✅ | [Invert Binary Tree](./07-Trees/01-Invert-Binary-Tree) | Python | $O(n)$ | $O(n)$ |
| ✅ | [Maximum Depth of Binary Tree](./07-Trees/02-Maximum-Depth-of-Binary-Tree/) | | | |
| ✅ | [](./07-Trees/03-Diameter-of-Binary-Tree/) | | | |
| ✅ | [](./07-Trees/04-Balanced-Binary-Tree/) | | | |
| ✅ | [](./07-Trees/05-Same-Tree/) | | | |
| ✅ | [](./07-Trees/06-Subtree-of-Another-Tree/) | | | |
| ✅ | [](./07-Trees/07-Lowest-Common-Ancestor-of-a-Binary-Search-Tree/) | | | |
| ✅ | [](./07-Trees/08-Binary-Tree-Level-Order-Traversal/) | | | |
| ✅ | [](./07-Trees/09-Binary-Tree-Right-Side-View/) | | | |
| ✅ | [](./07-Trees/10-Count-Good-Nodes-In-Binary-Tree/) | | | |
| ✅ | [](./07-Trees/11-Validate-Binary-Search-Tree/) | | | |
| ✅ | [](./07-Trees/12-Kth-Smallest-Element-In-a-Bst/) | | | |
| ✅ | [](./07-Trees/13-Construct-Binary-Tree-From-Preorder-And-Inorder-Traversal/) | | | |
| ✅ | [](./07-Trees/14-Binary-Tree-Maximum-Path-Sum/) | | | |
| ✅ | [](./07-Trees/15-Serialize-And-Deserialize-Binary-Tree/) | | | |
</details>

<details>
<summary><b>8. Heap Priority Queue [7 / 7]</b></summary>
<br>

| Status | Problem | Language | Time | Space |
| :---: | :--- | :---: | :---: | :---: |
| ✅ | [](./08-Heap-Priority-Queue/01-Kth-Largest-Element_in_a_Stream/) | | | |
| ✅ | [](./08-Heap-Priority-Queue/02-Last-Stone-Weight/) | | | |
| ✅ | [](/08-Heap-Priority-Queue/03-K-Closest-Points-to-Origin/) | | | |
| ✅ | [](/08-Heap-Priority-Queue/04-Kth-Largest-Element-In-An-Array/) | | | |
| ✅ | [](/08-Heap-Priority-Queue/05-Task-Scheduler/) | | | |
| ✅ | [](/08-Heap-Priority-Queue/06-Design-Twitter/) | | | |
| ✅ | [](/08-Heap-Priority-Queue/07-Find-Median-From-Data-Stream/) | | | |

</details>


<details>
<summary><b>17. Math and Geometry [8 / 8]</b></summary>
<br>

| Status | Problem | Language | Time | Space |
| :---: | :--- | :---: | :---: | :---: |
| ✅ | []() | | | |
| ✅ | []() | | | |
| ✅ | []() | | | |
| ✅ | []() | | | |
| ✅ | []() | | | |
| ✅ | []() | | | |
| ✅ | []() | | | |
</details>



<details>
<summary><b>18. Bit-Manipulation [7 / 7]</b></summary>
<br>

| Status | Problem | Language | Time | Space |
| :---: | :--- | :---: | :---: | :---: |
| ✅ | []() | | | |
| ✅ | []() | | | |
| ✅ | []() | | | |
| ✅ | []() | | | |
| ✅ | []() | | | |
| ✅ | []() | | | |
| ✅ | []() | | | |
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
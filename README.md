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
<summary><b>1. Arrays & Hashing [2 / 9]</b></summary>
<br>

| Status | Problem | Language | Time | Space |
| :---: | :--- | :---: | :---: | :---: |
| ✅ | [Contains Duplicate](./01-Arrays-and-Hashing/01-Contains-Duplicate) | Python | $O(n)$ | $O(n)$ |
| ✅ | [Valid Anagram](./01-Arrays-and-Hashing/02-Valid-Anagram) | Python | $O(n + m)$ | $O(1)$ |
| ⬜️ | Two Sum | | | |
| ⬜️ | Group Anagrams | | | |

</details>

<details>
<summary><b>2. Two Pointers [1 / 5]</b></summary>
<br>

| Status | Problem | Language | Time | Space |
| :---: | :--- | :---: | :---: | :---: |
| ✅ | [Valid Palindrome](./02-Two-Pointers/01-Valid-Palindrome) | Python | $O(n)$ | $O(1)$ |
| ⬜️ | Two Sum II | | | |
| ⬜️ | 3Sum | | | |

</details>

<details>
<summary><b>3. Sliding Window [1 / 6]</b></summary>
<br>

| Status | Problem | Language | Time | Space |
| :---: | :--- | :---: | :---: | :---: |
| ✅ | [Best Time to Buy and Sell Stock](./03-Sliding-Window/01-Best-Time-to-Buy-and-Sell-Stock) | Python | $O(n)$ | $O(1)$ |
| ⬜️ | Longest Substring Without Repeating Characters | | | |

</details>

<details>
<summary><b>4. Stack [1 / 7]</b></summary>
<br>

| Status | Problem | Language | Time | Space |
| :---: | :--- | :---: | :---: | :---: |
| ✅ | [Valid Parentheses](./04-Stack/01-Valid-Parentheses) | Python | $O(n)$ | $O(n)$ |
| ⬜️ | Min Stack | | | |

</details>

<details>
<summary><b>5. Binary Search [1 / 7]</b></summary>
<br>

| Status | Problem | Language | Time | Space |
| :---: | :--- | :---: | :---: | :---: |
| ✅ | [Binary Search](./05-Binary-Search/01-Binary-Search) | Python | $O(\log n)$ | $O(1)$ |
| ⬜️ | Search a 2D Matrix | | | |

</details>

<details>
<summary><b>6. Linked List [1 / 11]</b></summary>
<br>

| Status | Problem | Language | Time | Space |
| :---: | :--- | :---: | :---: | :---: |
| ✅ | [Reverse Linked List](./06-Linked-List/01-Reverse-Linked-List) | Python | $O(n)$ | $O(1)$ |
| ⬜️ | Merge Two Sorted Lists | | | |

</details>

<details>
<summary><b>7. Trees [1 / 15]</b></summary>
<br>

| Status | Problem | Language | Time | Space |
| :---: | :--- | :---: | :---: | :---: |
| ✅ | [Invert Binary Tree](./07-Trees/01-Invert-Binary-Tree) | Python | $O(n)$ | $O(n)$ |
| ⬜️ | Maximum Depth of Binary Tree | | | |

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
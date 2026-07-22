# 🚀 NeetCode 150 - Professional Python Portfolio
Welcome to my NeetCode 150 showcase repository! This repository contains clean, optimized Python solutions and robust, enterprise-grade test suites for the top 150 algorithmic patterns.

Instead of a messy collection of unorganized scripts, this project is structured to demonstrate professional software engineering standards, Test-Driven Development (TDD), and meticulous QA practices.

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
└── 07-Trees/
```
## 🛠️ Engineering Standards
Every single problem folder in this repository is treated as an independent module complete with:

Production-Ready Code (solution.py): Written in Python with full type hints (typing module) for static analysis, optimal time and space complexity, and clean docstrings.

Comprehensive Unit Tests (test_solution.py): Leverages pytest with parameterized test suites containing 15+ distinct test cases per problem. This covers standard examples, boundary limits, negative constraints, and complex logical edge cases.

Dedicated Documentation (README.md): Contains problem descriptions, complexity analysis, approach breakdowns, and instructions for running local checks.

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

## 📈 Progress Tracker
| Status | Category         | Problem                         | Language |
|---------|------------------|---------------------------------|----------|
| ✅      | Arrays & Hashing | Contains Duplicate              | Python   |
| ✅      | Arrays & Hashing | Valid Anagram                   | Python   |
| ✅      | Two Pointers     | Valid Palindrome                | Python   |
| ✅      | Sliding Window   | Best Time to Buy and Sell Stock | Python   |
| ✅      | Stack            | Valid Parentheses               | Python   | 
| ✅      | Binary Search    | Binary Search                   | Python   | 
| ✅      | Linked List      | Reverse Linked List             | Python   |
| ✅      | Trees            | Invert Binary Tree              | Python   | 


(...and continually expanding through the complete NeetCode roadmap!)
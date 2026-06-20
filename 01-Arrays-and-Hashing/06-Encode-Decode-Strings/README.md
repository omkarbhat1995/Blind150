# Encode and Decode Strings

**Difficulty:** Medium  
**Category:** Arrays & Hashing  

## 📝 Problem Statement

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

### Examples

**Example 1:**
> **Input:** `strs = ["Hello", "World"]`  
> **Output:** `["Hello", "World"]`

**Example 2:**
> **Input:** `strs = [""]`  
> **Output:** `[""]`

### Constraints
* `0 <= strs.length < 100`
* `0 <= strs[i].length < 200`
* `strs[i]` contains any possible characters out of 256 valid ASCII characters.

---

## 💡 Approach

A naive approach would be to join the strings using a unique delimiter, like a comma `,` or a hash `#` (e.g., `Hello#World`). However, the constraints state that the strings can contain *any* ASCII character. If the input array is `["Hello#", "World"]`, a simple split on `#` will corrupt the data during decoding.

To guarantee safe encoding and decoding regardless of the characters inside the strings, we use **Length-Prefix Encoding**. 

For every string, we record its length, followed by a delimiter (like `#`), followed by the actual string. 
For example: `["Hello", "World"]` becomes `5#Hello5#World`. 

When decoding, we:
1. Read the integer until we hit the `#` delimiter.
2. Read exactly that many characters to extract the string.
3. Repeat the process. 
Because we strictly read the exact character count, we completely ignore any `#` characters that might be hiding inside the actual strings.

### ⏱️ Complexity
* **Time Complexity:** `O(n)` — Where `n` is the total number of characters across all strings. We iterate through every character exactly once during encoding and once during decoding.
* **Space Complexity:** `O(n)` — We allocate a new string to hold the encoded data and a new array to hold the decoded data.

---

## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:

```bash
pytest 01-Arrays-and-Hashing/06-Encode-and-Decode-Strings/test_solution.py -v
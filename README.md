# Hash Table Ransom Note Lab

### Overview

This project implements a solution to the classic **Ransom Note** problem using a **hash table (dictionary)** approach in Python.

The goal is to determine whether a target string (`ransomNote`) can be constructed using the characters available in another string (`magazine`), where each character in the magazine may only be used once.

This lab reinforces:
- Frequency counting with hash tables
- Efficient lookup and comparison
- Clear boolean logic driven by test cases

---

### Features

- Determines if a ransom note can be constructed from available characters
- Correctly handles repeated characters
- Efficient time complexity using hash tables
- Fully tested with short and long string cases

---

### Function Behavior

The function implemented is:

- `can_construct(ransomNote: str, magazine: str) -> bool`

Rules enforced:
- Each character in `magazine` may be used only once
- All characters required by `ransomNote` must exist in sufficient quantity
- Returns `True` if construction is possible, otherwise `False`

---

### Example

**Input**
ransomNote = "aa"
magazine = "aab"

**Output**
True

**Input**
ransomNote = "aa"
magazine = "ab"

**Output**
False

---

### Technologies & Tools Used

#### Language
- Python 3

#### Core Concepts
- Hash tables (Python dictionaries / Counter)
- Frequency counting
- Time complexity optimization

#### Testing
- Pytest

#### Tooling
- Git & GitHub

---

### File Structure

All paths are listed relative to the project root.

- hash-table-ransom-note-lab/__pycache__/
- hash-table-ransom-note-lab/.pytest_cache/
- hash-table-ransom-note-lab/.gitignore
- hash-table-ransom-note-lab/ransom_note.py
- hash-table-ransom-note-lab/test_ransom_note.py
- hash-table-ransom-note-lab/README.md

---

### Key Files Explained

#### ransom_note.py
- Implements the `can_construct` function
- Uses a hash table to count character frequencies
- Ensures magazine characters are not reused beyond availability

#### test_ransom_note.py
- Contains test cases for both short and long input strings
- Validates correctness across multiple edge cases

---

### Testing Notes

- Tests validate correct handling of repeated characters
- Longer sentence-based inputs ensure robustness
- No external dependencies are required

Run tests with:
pytest

---

### License

Educational use only.  
Intended for learning hash table usage and problem-solving with frequency counting.

### Additional notes:
- Project passed through ChatGPT for syntax and grammatical error checking and for writing this README.md. Everything was double checked for accuracy and readability prior to submission.
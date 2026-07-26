# LAB-08 - Sudoku

## 📝 User Story
**As a** Python student preparing for the PCAP certification,  
**I want to** implement a program that validates a 9x9 Sudoku board,  
**So that** I can improve my skills in string-to-list conversion, multi-dimensional list traversal, and implementing complex logical constraints.

---

## ✅ Acceptance Criteria
*These are the conditions that must be met for this lab to be considered "done".*

**Scenario: Valid Sudoku board**
- **Given** the user inputs a valid 9x9 Sudoku configuration:
```text
295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672
```
- **When** the validation program is executed
- **Then** it must output: 
```text
Yes
```

**Scenario: Invalid Sudoku board with duplicate numbers in columns/rows/squares**
- **Given** the user inputs an invalid 9x9 Sudoku configuration:
```text
195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671
```
- **When** the validation program is executed
- **Then** it must output: 
```text
No
```

---

## 🛠️ Technical Notes
- **Implementation Details:** The program expects 9 consecutive string inputs, each containing exactly 9 digits. It builds a two-dimensional structure (a list of lists or a list of strings). The validation logic must check three strict conditions: 
  1. Every row contains all digits from 1 to 9 exactly once.
  2. Every column contains all digits from 1 to 9 exactly once.
  3. Every 3x3 sub-square contains all digits from 1 to 9 exactly once. 
  *Note: The official prompt mentions digits "0 to 9", but standard Sudoku and the provided test data use 1 to 9.* Python's `set()` or sorting methods are ideal for ensuring there are no missing or duplicate digits.
- **Complexity:** 
  - Time Complexity: $O(N^2)$, where $N$ is the dimension of the board (9). Because the board is fixed at 9x9, the execution time is technically a constant $O(1)$, but algorithmically scales quadratically with board width.
  - Space Complexity: $O(N^2)$ to store the 9x9 matrix in memory.
- **Dependencies:** Pure Python standard library only. No external modules required.

## 🔗 Official Reference
This project contains my own implementation, documentation, and automated tests for the following educational activity:

- [Python Essentials 2 — Official Lab: Sudoku](https://edube.org/learn/pe-2/sudoku-1)

The original exercise statement is not reproduced in this repository. Access to the course content may require an Edube account.

## 🚀 Future Enhancements
While the current MVP validates a perfectly formatted 9x9 input, future iterations could include:

- **Robust Input Sanitization:** Implement a validation loop that intercepts inputs with incorrect lengths (e.g., fewer than 9 characters), non-digit characters (like letters or punctuation), and prompts the user to re-enter that specific row instead of crashing.
- **Dynamic Board Sizing:** Generalize the core logic to support other standard Sudoku sizes, such as 4x4 (Sub-squares of 2x2) or 16x16 (Sub-squares of 4x4), utilizing dynamic nested loops based on a defined board size variable.
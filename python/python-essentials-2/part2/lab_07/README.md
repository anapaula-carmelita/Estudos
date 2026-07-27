# LAB-07 - Find a Word

## 📝 User Story
**As a** Python student preparing for the PCAP certification,  
**I want to** implement a program that checks whether all characters of a word appear sequentially inside a target string,  
**So that** I can master sequential string searching algorithms and the two-argument `find()` method.

---

## ✅ Acceptance Criteria
*These are the conditions that must be met for this lab to be considered "done".*

**Scenario: Word characters present in order**
- **Given** the user inputs the word `"donor"` and the target string `"Nabucodonosor"`
- **When** the search program is executed
- **Then** it must output: 
```text
Yes
```

**Scenario: Word characters missing or out of order**
- **Given** the user inputs the word `"donut"` and the target string `"Nabucodonosor"`
- **When** the search program is executed
- **Then** it must output: 
```text
No
```

**Scenario: Case-insensitive search with random characters**
- **Given** the user inputs the word `"dog"` and the target string `"vcxzxduybfdsobywuefgas"`
- **When** the search program is executed
- **Then** it must output: 
```text
Yes
```

---

## 🛠️ Technical Notes
- **Implementation Details:** The program reads two separate string inputs: the search word and the target text. Both strings are converted to lowercase to ensure case-insensitivity. It tracks the current search starting index (initially `0`) and iterates through each character of the search word. Using the two-argument `str.find(char, start_index)` method, it looks for the character. If found, `start_index` updates to `found_index + 1` to ensure sequential matching. If any character yields `-1`, the search stops and outputs `No`.
- **Complexity:** 
  - Time Complexity: $O(n \cdot m)$ worst-case, where $n$ is the length of the search word and $m$ is the length of the target string.
  - Space Complexity: $O(n + m)$ to store the normalized lowercased strings.
- **Dependencies:** Pure Python standard library only. No external modules required.

## 🔗 Official Reference
This project contains my own implementation, documentation, and automated tests for the following educational activity:

- [Python Essentials 2 — Official Lab: Find a word](https://edube.org/learn/pe-2/find-a-word-1)

The original exercise statement is not reproduced in this repository. Access to the course content may require an Edube account.

## 🚀 Future Enhancements
While the current implementation relies on the two-argument `find()` method for linear traversal, future iterations could include:

- **Regular Expressions (RegEx) Alternative:** Re-implement the search logic using Python's `re` module by dynamically constructing a pattern (e.g., `.*d.*o.*g.*`) to achieve concise pattern matching.
- **Match Index Reporting:** Extend the output to return the exact start and end positions in the target string where the hidden word was matched, providing visual feedback to the user.
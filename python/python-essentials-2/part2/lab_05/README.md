# LAB-05 - Anagrams

## 📝 User Story
**As a** Python student preparing for the PCAP certification,  
**I want to** implement an anagram checker program that normalizes case, ignores spaces, and compares string inputs,  
**So that** I can improve my skills in string manipulation, converting strings to lists, and sorting algorithms.

---

## ✅ Acceptance Criteria
*These are the conditions that must be met for this lab to be considered "done".*

**Scenario: Valid anagram pair with mixed case**
- **Given** the user inputs the first text `"Listen"` and the second text `"Silent"`
- **When** the anagram checker program is executed
- **Then** it must print the output: 
```text
Anagrams
```

**Scenario: Non-anagram pair**
- **Given** the user inputs the first text `"modern"` and the second text `"norman"`
- **When** the anagram checker program is executed
- **Then** it must print the output: 
```text
Not anagrams
```

**Scenario: Edge Case - Empty strings or spaces only**
- **Given** the user inputs two empty strings `""` or strings containing only whitespaces
- **When** the program is executed
- **Then** it must treat them as invalid and print: 
```text
Not anagrams
```

---

## 🛠️ Technical Notes
- **Implementation Details:** The program reads two separate text inputs. For each string, it removes all whitespace characters and converts all letters to lowercase to ensure case-insensitivity. It then converts the cleaned strings into lists of characters and sorts them (or compares character frequencies). If both sorted character representations match and are non-empty, the inputs are confirmed to be anagrams.
- **Complexity:** 
  - Time Complexity: $O(n \log n)$, where $n$ is the length of the string, due to sorting character lists (or $O(n)$ if using character frequency counts).
  - Space Complexity: $O(n)$ to store the cleaned strings and sorted character lists.
- **Dependencies:** Pure Python standard library only. No external modules required.

## 🔗 Official Reference
This project contains my own implementation, documentation, and automated tests for the following educational activity:

- [Python Essentials 2 — Official Lab: Anagrams](https://edube.org/learn/pe-2/lab-anagrams-3)

The original exercise statement is not reproduced in this repository. Access to the course content may require an Edube account.

## 🚀 Future Enhancements
While the current implementation successfully handles case normalization and whitespace removal, future iterations could include:

- **Punctuation and Special Character Filtering:** Extend the normalization step to automatically strip punctuation marks (e.g., periods, commas, or exclamation points) so that full sentences with symbols can be compared accurately.
- **Linear Time Complexity ($O(n)$) Optimization:** Replace list sorting with a hash-map or frequency dictionary approach (e.g., using `collections.Counter` or a custom dictionary) to achieve linear time complexity instead of $O(n \log n)$.
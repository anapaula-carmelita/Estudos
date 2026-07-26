# LAB-04 - Palindromes

## 📝 User Story
**As a** Python student preparing for the PCAP certification,  
**I want to** implement a palindrome checker that normalizes case and ignores spaces,  
**So that** I can improve my string manipulation skills and explore non-obvious, efficient algorithmic solutions.

---

## ✅ Acceptance Criteria
*These are the conditions that must be met for this lab to be considered "done".*

**Scenario: Valid palindrome sentence with spaces and mixed case**
- **Given** the user inputs the text `"Ten animals I slam in a net"`
- **When** the palindrome program is executed
- **Then** it must print the output: 
```text
It's a palindrome
```

**Scenario: Non-palindrome sentence**
- **Given** the user inputs the text `"Eleven animals I slam in a net"`
- **When** the palindrome program is executed
- **Then** it must print the output: 
```text
It's not a palindrome
```

**Scenario: Edge Case - Empty string**
- **Given** the user inputs an empty string `""`
- **When** the program is executed
- **Then** it must treat it as invalid and print: 
```text
It's not a palindrome
```

---

## 🛠️ Technical Notes
- **Implementation Details:** The program reads a line of text from the user, strips or ignores all whitespace characters, and converts all letters to lowercase to ensure case-insensitivity. It then checks if the normalized sequence reads the same forwards and backwards. Solutions can explore multiple approaches, such as string slicing (e.g., `s[::-1]`), two-pointer techniques, or deque-based comparisons.
- **Complexity:** 
  - Time Complexity: $O(n)$, where $n$ is the length of the input string, as characters are processed in a linear pass. 
  - Space Complexity: $O(n)$ to store the cleaned string or character collections.
- **Dependencies:** Pure Python standard library only. No external modules required.

## 🔗 Official Reference
This project contains my own implementation, documentation, and automated tests for the following educational activity:

- [Python Essentials 2 — Official Lab: Palindromes](https://edube.org/learn/pe-2/lab-palindromes-4)

The original exercise statement is not reproduced in this repository. Access to the course content may require an Edube account.

## 🚀 Future Enhancements
While the current implementation successfully handles standard whitespace removal and case-insensitivity, future iterations could include:

- **Punctuation Filtering:** Extend the normalization logic to automatically strip punctuation marks (such as commas, periods, or apostrophes) so that phrases with punctuation (like `"A man, a plan, a canal: Panama"`) are validated correctly without manual preprocessing.
- **Performance Benchmarking:** Compare the execution time and memory footprint of different palindrome-checking approaches (e.g., slicing vs. iterative two-pointer traversal) to evaluate optimization trade-offs.
# LAB-02 - A LED Display

## 📝 User Story
**As a** Python student preparing for the PCAP certification,  
**I want to** implement a function called `leddisplay()`,  
**So that** I can improve my skills in multidimensional list indexing, loop manipulation, and multiline string concatenation.

---

## ✅ Acceptance Criteria
*These are the conditions that must be met for this lab to be considered "done".*

**Scenario: Two-digit sequence**
- **Given** the function receives the string `"01"`
- **When** `leddisplay()` is executed
- **Then** it must return the output: 
```text
###   # 
# #   # 
# #   # 
# #   # 
###   # 

```

**Scenario: Standard sequence**
- **Given** the function receives the string `"123"`
- **When** `leddisplay()` is executed
- **Then** it must return the output: 
```text
  # ### ### 
  #   #   # 
  # ### ### 
  # #     # 
  # ### ### 

```

**Scenario: Large number sequence**
- **Given** the function receives the string `"9081726354"`
- **When** `leddisplay()` is executed
- **Then** it must return the output: 
```text
### ### ###   # ### ### ### ### ### # # 
# # # # # #   #   #   # #     # #   # # 
### # # ###   #   # ### ### ### ### ### 
  # # # # #   #   # #   # #   #   #   # 
### ### ###   #   # ### ### ### ###   # 

```

---

## 🛠️ Technical Notes
- **Implementation Details:** The function utilizes a predefined multidimensional list to store the 5-line ASCII patterns for digits 0 through 9. It iterates through the input string to convert characters into integer indices. Then, using a nested loop, it maps these indices to construct the final text line by line, appending a newline (`\n`) at the end of each of the 5 rows.
- **Complexity:** 
  - Time Complexity: $O(n)$, where $n$ is the length of the string, since it requires a linear pass to process the digits. 
  - Space Complexity: $O(n)$ to store the temporary integer list and to build the resulting multiline string.
- **Dependencies:** Pure Python standard library only. No external modules required.

## 🔗 Official Reference
This project contains my own implementation, documentation, and automated tests for the following educational activity:

- [Python Essentials 2 — Official Lab: A LED Display](https://edube.org/learn/pe-2/a-led-display-1)

The original exercise statement is not reproduced in this repository. Access to the course content may require an Edube account.

## 🚀 Future Enhancements
While the current MVP successfully converts numerical strings into an ASCII art representation, future iterations could include:

- **Error Handling:** Add validation to handle non-digit characters (e.g., letters or punctuation) gracefully. Currently, passing a character like `"A"` would raise a `ValueError`. This could be improved by ignoring invalid characters or rendering a custom "unknown" character (like a `?`).
- **Dynamic Scaling:** Modify the function to accept a `scale` parameter (e.g., `leddisplay(text, scale=2)`), allowing the digits to be rendered in larger dimensions dynamically.
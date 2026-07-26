# LAB-03 - Improved Caesar Cipher

## 📝 User Story
**As a** Python student preparing for the PCAP certification,  
**I want to** implement an advanced Caesar cipher program with dynamic shift validation and case preservation,  
**So that** I can improve my skills in string manipulation, ASCII code conversion (`ord()` and `chr()`), and robust input validation.

---

## ✅ Acceptance Criteria
*These are the conditions that must be met for this lab to be considered "done".*

**Scenario: Standard text with a positive shift of 2**
- **Given** the user inputs the text `"abcxyzABCxyz 123"` and the shift value `2`
- **When** the cipher program is executed
- **Then** it must print the encoded output: 
```text
cdezabCDEzab 123
```

**Scenario: Sentence with spaces and mixed case with a shift of 25**
- **Given** the user inputs the text `"The die is cast"` and the shift value `25`
- **When** the cipher program is executed
- **Then** it must print the encoded output: 
```text
Sgd chd hr bzrs
```

**Scenario: Edge Case - Invalid shift value out of range**
- **Given** the user inputs a shift value outside the range 1 to 25 (e.g., `0`, `26`, or a non-integer)
- **When** the program prompts for the shift
- **Then** it must continuously force the user to enter a valid integer from `1` to `25` without crashing or accepting bad data.

---

## 🛠️ Technical Notes
- **Implementation Details:** The program reads a line of text and an integer shift value. It iterates through each character, checking if it is alphabetical. Using built-in functions like `ord()` and `chr()`, it shifts the character code while ensuring lower-case and upper-case letters wrap correctly around the alphabet (a-z and A-Z). Non-alphabetical characters (such as spaces and digits) remain completely untouched. Input validation loops ensure the shift value strictly falls between 1 and 25 inclusive.
- **Complexity:** 
  - Time Complexity: $O(n)$, where $n$ is the length of the input string, since each character is processed in a single pass. 
  - Space Complexity: $O(n)$ to store the input string and build the resulting encrypted text.
- **Dependencies:** Pure Python standard library only. No external modules required.

## 🔗 Official Reference
This project contains my own implementation, documentation, and automated tests for the following educational activity:

- [Python Essentials 2 — Official Lab: Improved Caesar Cipher](https://edube.org/learn/pe-2/lab-improving-the-caesar-cipher-3)

The original exercise statement is not reproduced in this repository. Access to the course content may require an Edube account.

## 🚀 Future Enhancements
While the current implementation successfully handles case preservation and secure range validation for the Caesar cipher, future iterations could include:

- **Decryption Functionality:** Add a complementary `decrypt()` function or an interactive mode that allows users to reverse the cipher by providing the encoded text and the original shift value.
- **Support for Full ASCII Range:** Expand the cipher logic to safely handle extended characters or punctuation marks using configurable substitution rules or dynamic mapping tables.
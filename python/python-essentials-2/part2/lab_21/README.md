# LAB-21 - Reading Ints Safely

## 📝 User Story
**As a** Python student preparing for the PCAP certification,  
**I want to** implement a robust integer input function with exception handling and range validation,  
**So that** I can build safe user input environments and master `try-except` exception control blocks.

---

## ✅ Acceptance Criteria
*These are the conditions that must be met for this lab to be considered "done".*

**Scenario: Non-integer input handling**
- **Given** the function prompts the user for a number between `-10` and `10`
- **When** the user inputs a non-integer string like `"asd"`
- **Then** it must print the error message:
```text
Error: wrong input
```
and prompt the user again until a valid integer is entered.

**Scenario: Out-of-range integer handling**
- **Given** the function prompts the user for a number between `-10` and `10`
- **When** the user inputs a number outside the range like `100`
- **Then** it must print the error message:
```text
Error: the value is not within permitted range (-10..10)
```
and prompt the user again until a valid integer within the range is entered.

**Scenario: Valid integer input**
- **Given** the function prompts the user for a number between `-10` and `10`
- **When** the user inputs a valid integer like `1`
- **Then** the function must return the integer value `1`.

---

## 🛠️ Technical Notes
- **Implementation Details:** The function accepts three parameters: `prompt` (string), `min` (integer), and `max` (integer). It uses an infinite `while True` loop containing a `try-except ValueError` block to handle string-to-integer conversion. If `int()` raises a `ValueError`, it catches the exception and prints `"Error: wrong input"`. If the conversion succeeds, it verifies if `min <= value <= max`. If outside the boundaries, it displays `"Error: the value is not within permitted range (min..max)"`. The loop terminates and returns the valid `int` once all criteria are met.
- **Complexity:** 
  - Time Complexity: $O(1)$ per attempt, as type conversion and range checking run in constant time.
  - Space Complexity: $O(1)$ auxiliary space.
- **Dependencies:** Pure Python standard library only. No external modules required.

## 🔗 Official Reference
This project contains my own implementation, documentation, and automated tests for the following educational activity:

- [Python Essentials 2 — Official Lab: Reading ints safely](https://edube.org/learn/pe-2/reading-ints-safely-4)

The original exercise statement is not reproduced in this repository. Access to the course content may require an Edube account.

## 🚀 Future Enhancements
While the current implementation safely intercepts invalid inputs using console printing, future iterations could include:

- **Custom Exception Raising:** Refactor the function to raise custom exception classes (e.g., `OutOfRangeError`) instead of relying directly on `print()` calls, allowing parent modules or test suites to handle errors programmatically.
- **Support for Optional Type Casting:** Extend the parameter list to accept a `data_type` argument (such as `float` or `int`), enabling flexible numerical validation across different user input requirements.
# LAB - A LED Display

## 📝 User Story
**As a** Python student preparing for the PCAP certification,  
**I want to** write a program that simulates a seven-segment LED display using strings,  
**So that** I can improve my skills in string operations and learn how to represent non-textual data through string patterns and lists.

---

## ✅ Acceptance Criteria
*These are the conditions that must be met for this lab to be considered "done".*

**Scenario: Short non-negative integer input**
- **Given** the user inputs the string `"123"`
- **When** the LED display program processes the input
- **Then** it must output the correct 5-line string representation using `#` and spaces for the digits 1, 2, and 3 side-by-side.

**Scenario: Long non-negative integer input**
- **Given** the user inputs the string `"9081726354"`
- **When** the LED display program processes the input
- **Then** it must output the correct 5-line string representation mapping all these digits accurately and sequentially.

**Scenario: Edge Case - Single digit**
- **Given** the user inputs a single digit, such as `"8"`
- **When** the program processes the input
- **Then** it must output the 5-line string representation with all LEDs lit for that specific digit.

---

## 🛠️ Technical Notes
- **Implementation Details:** A highly recommended approach is to use a list containing the string patterns for all ten decimal digits. Since each digit's visual representation consists of 5 rows, the program needs to extract each digit from the user's input, map it to the corresponding pattern, and iterate line by line (from 1 to 5) to concatenate and print the corresponding segments for all digits side-by-side.
- **Complexity:** Time Complexity: $O(n)$, where $n$ is the number of digits in the input string, as the program needs to process each digit for each of the 5 rows. Space Complexity: $O(1)$ if printing directly, or $O(n)$ if storing the final concatenated rows in memory before printing.
- **Dependencies:** Pure Python standard library only. No external modules required.

---

## 💻 Proposed Solution
```python
#  File name: lab_02_led_display.py
#  Description: A possible solution for the 'A LED Display' LAB from Python Essentials 2
#  Author: Ana Paula da Silva Souza
#  Date: 2026-07-22
#  Version: 1.0
#  License: Apache
#

# TODO: Implement the solution here
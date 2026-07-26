# LAB-06 - Digit of Life

## 📝 User Story
**As a** Python student preparing for the PCAP certification,  
**I want to** implement a program that calculates the single-digit sum (Digit of Life) from a birthday string,  
**So that** I can strengthen my skills in type conversion between strings and integers and master loop-based reduction logic.

---

## ✅ Acceptance Criteria
*These are the conditions that must be met for this lab to be considered "done".*

**Scenario: Date requiring multiple reduction steps**
- **Given** the user inputs the date string `"19991229"`
- **When** the Digit of Life program is executed
- **Then** it must output: 
```text
6
```

**Scenario: Date requiring a single step**
- **Given** the user inputs the date string `"20000101"`
- **When** the Digit of Life program is executed
- **Then** it must output: 
```text
4
```

**Scenario: Date in a different format (YYYYDDMM)**
- **Given** the user inputs the date string `"20170101"`
- **When** the Digit of Life program is executed
- **Then** it must output: 
```text
3
```

---

## 🛠️ Technical Notes
- **Implementation Details:** The program reads a string representing a birthday date. It iterates through the string characters, converting each digit to an integer and summing them up. If the resulting sum has a length greater than 1 (more than one digit), the process repeats using the new sum converted back to a string until a single-digit integer remains.
- **Complexity:** 
  - Time Complexity: $O(d)$, where $d$ is the number of digits in the date string (effectively $O(1)$ for standard 8-digit date formats).
  - Space Complexity: $O(1)$ auxiliary space since intermediate string/int conversions hold a fixed, minimal amount of digits.
- **Dependencies:** Pure Python standard library only. No external modules required.

## 🔗 Official Reference
This project contains my own implementation, documentation, and automated tests for the following educational activity:

- [Python Essentials 2 — Official Lab: Digit of Life](https://edube.org/learn/pe-2/lab-the-digit-of-life-3)

The original exercise statement is not reproduced in this repository. Access to the course content may require an Edube account.

## 🚀 Future Enhancements
While the current implementation successfully reduces the digit sum iteratively using string conversions, future iterations could include:

- **Strict Date & Format Validation:** Add regex or `datetime` parsing to verify that the user input consists strictly of numbers and represents a real calendar date before calculating the digit.
- **Digital Root Mathematical Optimization:** Replace string-loop conversion with the modulo-9 formula for Digital Root ($1 + (n - 1) \pmod 9$), achieving immediate $O(1)$ arithmetic calculation without needing iterative string conversion loops.
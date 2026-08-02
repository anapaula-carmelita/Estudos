# [Lab 16] - Character Frequency Histogram

## 📝 User Story

**As a** Python student / developer,
**I want to** create a program that asks for a text file's name, reads its content, and counts the frequency of all Latin letters (treating lower- and upper-case letters as equal),
**So that** I can display a simple histogram in alphabetical order showing how rare or frequent each letter is, which can be useful for cryptographic analysis.

---

## ✅ Acceptance Criteria

**Scenario: Successful reading and letter counting**
* **Given** a valid test text file containing the line "aBc"
* **When** the user runs the program and inputs the name of this file (e.g., `samplefile.txt`)
* **Then** the program should print the histogram in alphabetical order with only the letters that have a count greater than zero, in the following format:

    a -> 1
    b -> 1
    c -> 1

**Scenario: Handling special characters and numbers**
* **Given** a text file containing numbers, spaces, or punctuation symbols
* **When** the program processes the counting
* **Then** these non-Latin characters must be ignored and should not appear in the final histogram.

**Scenario: Edge Case/Error Handling (File Not Found)**
* **Given** a filename that does not exist in the directory
* **When** the program attempts to read the file
* **Then** the program should handle the exception (e.g., `FileNotFoundError`) gracefully, informing the user that the reading was not possible.

---

## 🛠️ Technical Notes

* **Implementation Details:** It is recommended to use a **dictionary** (`dict`) as the data collection medium to store the counts, where the keys will be the lowercase letters (obtained using `.lower()`) and the values will be the counters. To print in alphabetical order, the dictionary keys can be sorted before the print loop. The `.isalpha()` method can be useful to check if a character is a letter.
* **Complexity:** 
  * **Time:** O(N), where N is the number of characters in the file, as each character is read and processed iteratively.
  * **Space:** O(1), since the maximum size of the dictionary will be constant at 26 entries (representing the Latin alphabet).
* **Dependencies:** Only standard Python library functions and methods (File I/O).
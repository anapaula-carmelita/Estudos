# [Lab 18] - Evaluating Students' Results

## 📝 User Story

**As a** Python student / developer,
**I want to** create a program that reads a text file containing students' names and their respective class points, aggregates the total points for each student, and prints a sorted report,
**So that** I can easily track and evaluate students' total scores while ensuring the program is fully protected against file and data formatting errors through custom exceptions.

---

## ✅ Acceptance Criteria

**Scenario: Successful aggregation and sorted report**
* **Given** a valid text file (e.g., `samplefile.txt`) where each line contains a First Name, Last Name, and Points separated by whitespaces
* **When** the user inputs the file name and the program processes the data
* **Then** the program should aggregate the points for students appearing multiple times and print a report sorted alphabetically by the students' names, formatted exactly like:

    Andrew Cox 	 1.5
    Anna Boleyn 	 15.5
    John Smith 	 7.0

**Scenario: Error Handling - Bad Line Data**
* **Given** a file containing improperly formatted lines (e.g., missing elements, or points that cannot be converted to a float)
* **When** the program attempts to parse the corrupted line
* **Then** it must raise a custom exception (e.g., `BadLine`), immediately terminate the execution, and display the erroneous data/line to the user.

**Scenario: Error Handling - Empty File**
* **Given** a file that exists in the directory but is completely empty
* **When** the program opens and attempts to read it
* **Then** it must raise a custom exception (e.g., `FileEmpty`) and inform the user that the source file contains no data.

**Scenario: Error Handling - File Not Found**
* **Given** a filename input by the user that does not exist
* **When** the program attempts to open the file
* **Then** it must gracefully handle the standard `FileNotFoundError` (or a custom wrapper) and notify the user.

---

## 🛠️ Technical Notes

* **Implementation Details:** * Use a **dictionary** (`dict`) to store the students' data. The keys should be strings (e.g., concatenating First Name and Last Name, or using a tuple `(First, Last)`), and the values should be the accumulated points as `float`.
  * You must implement a **custom exception hierarchy**. For example, a base class `StudentsDataException(Exception)`, and two subclasses: `BadLine(StudentsDataException)` and `FileEmpty(StudentsDataException)`.
  * Use the string `.split()` method to separate the line elements by whitespace.
  * Sort the dictionary keys alphabetically before printing the final report.
* **Complexity:** 
  * **Time:** O(L + N log N), where L is the number of lines in the file (to read and aggregate) and N is the number of unique students (to sort the dictionary keys for the report).
  * **Space:** O(N), where N is the number of unique students stored in the dictionary.
* **Dependencies:** Standard Python library (File I/O, Exceptions).
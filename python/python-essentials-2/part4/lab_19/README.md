# [Lab 19] - Find a Directory!

## 📝 User Story

**As a** Python student / developer,
**I want to** write a program with a `find(path, dir)` function that recursively searches for a specific directory name starting from a given path,
**So that** I can practice interacting with the operating system using the `os` module and easily retrieve the absolute paths of the target directories.

---

## ✅ Acceptance Criteria

**Scenario: Successful Recursive Directory Search**
* **Given** a valid starting path (e.g., `./tree`) and a target directory name (e.g., `python`)
* **When** the `find(path, dir)` function is executed
* **Then** the program should recursively search all subdirectories and print the absolute paths of any directory matching the target name.
  *Example Output:*
  .../tree/python
  .../tree/cpp/other_courses/python
  .../tree/c/other_courses/python

**Scenario: Directory Not Found in Tree**
* **Given** a valid starting path but a target directory name that does not exist anywhere in the tree
* **When** the `find` function executes
* **Then** the program should complete its recursive search and terminate without printing any paths, gracefully handling the absence of the target.

**Scenario: Edge Case/Error Handling (Invalid Starting Path)**
* **Given** a starting `path` argument that is invalid or does not exist
* **When** the program attempts to list the contents of that path
* **Then** the program should handle the exception (e.g., using a `try-except` block for `FileNotFoundError` or checking `os.path.exists()`) and avoid a hard crash.

---

## 🛠️ Technical Notes

* **Implementation Details:** * The solution relies heavily on the `os` module. Key functions to use include `os.listdir()` to get directory contents, `os.path.join()` to construct paths properly across different OS platforms, `os.path.isdir()` to check if a path is a directory before recursing into it, and `os.path.abspath()` to print the final absolute path.
  * The `find` function must be **recursive**, meaning it should call itself whenever it encounters a new directory that does not match the target name, passing the new directory's path as the starting point.
* **Complexity:** 
  * **Time:** O(N), where N is the total number of files and directories within the starting path, as every node in the directory tree must be visited once.
  * **Space:** O(D), where D is the maximum depth of the directory tree, representing the memory used by the recursion call stack.
* **Dependencies:** Standard Python `os` module.
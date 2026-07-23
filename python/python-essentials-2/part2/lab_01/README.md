# US LAB-01 - Your Own Split Method

## 📝 User Story
**As a** Python student preparing for the PCAP certification,  
**I want to** implement my own version of the `split()` function called `mysplit()`,  
**So that** I can improve my string manipulation skills and understand how built-in string methods process whitespaces under the hood.

---

## ✅ Acceptance Criteria
*These are the conditions that must be met for this lab to be considered "done".*

**Scenario: Standard sentence with regular whitespaces**
- **Given** the function receives the string `"To be or not to be, that is the question"`
- **When** `mysplit()` is executed
- **Then** it must return the list: `['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question']`

**Scenario: Sentence with irregular spacing and attached punctuation**
- **Given** the function receives the string `"To be or not to be,that is the question"`
- **When** `mysplit()` is executed
- **Then** it must return the list: `['To', 'be', 'or', 'not', 'to', 'be,that', 'is', 'the', 'question']`

**Scenario: Single word string**
- **Given** the function receives the string `"abc"`
- **When** `mysplit()` is executed
- **Then** it must return the list: `['abc']`

**Scenario: Edge Case - Completely empty string**
- **Given** the function receives an empty string `""`
- **When** `mysplit()` is executed
- **Then** it must return an empty list: `[]`

**Scenario: Edge Case - String containing only whitespaces**
- **Given** the function receives a string with no characters other than spaces, like `"   "`
- **When** `mysplit()` is executed
- **Then** it must return an empty list: `[]`

**Scenario (extra): Multiple internal spaces mixed with characters**
- **Given** the function receives a string like the example `"Sacret     Heart, I trust in      You"`
- **When** `mysplit()` is executed
- **Then** it must return the list: `['Sacret', 'Heart,', 'I', 'trust', 'in', 'You']`

---

## 🛠️ Technical Notes
- **Implementation Details:** The function iterates through the string character by character using a loop. A temporary string variable accumulates characters for the current word. Upon encountering a whitespace, if the temporary string is not empty, it is appended to the result list and then reset. The built-in `split()` method is strictly forbidden.
- **Complexity:** Time Complexity: $O(n)$, where $n$ is the length of the string, since it requires a single pass. Space Complexity: $O(n)$ to store the resulting list of words.
- **Dependencies:** Pure Python standard library only. No external modules required.

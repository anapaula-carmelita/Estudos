## 📖 User Story: LAB 09 - Counting Stack

**As a** Python student preparing for the PCAP certification,
**I want to** create a subclass of the `Stack` class that counts the number of elements popped from the stack,
**So that** I can demonstrate my understanding of inheritance, data encapsulation (hidden properties), and method overriding in Object-Oriented Programming.

---

#### ✅ Acceptance Criteria (BDD)

**Scenario 1: Initializing the Counting Stack**
* **Given** a new instance of `CountingStack` is instantiated,
* **When** the constructor (`__init__`) is executed,
* **Then** a hidden/private property to count operations must be initialized to zero,
* **And** the superclass `Stack` constructor must be properly invoked to maintain the core stack behavior.

**Scenario 2: Popping elements and updating the counter**
* **Given** a `CountingStack` that has one or more elements pushed onto it,
* **When** the `pop()` method is called,
* **Then** the hidden counter property must be incremented by 1,
* **And** the method must return the popped value by leveraging the superclass's `pop()` method.

**Scenario 3: Retrieving the total pop count**
* **Given** a `CountingStack` that has undergone multiple `pop()` operations,
* **When** the `get_counter()` method is called,
* **Then** it must return the exact integer representing how many times elements were popped from this specific stack.

---

#### ⚙️ Technical & Business Rules

1. **Encapsulation:** The property used for counting must be strictly hidden/private (e.g., using double underscores like `__counter` or `__pop_counter`) to prevent outside manipulation.
2. **Inheritance:** The new class must inherit from the base `Stack` class provided in the Edube editor.
3. **Pops are Sufficient:** The lab assumes that counting just the `pop` operations is enough for this requirement; `push` operations do not need a separate counter increment.
4. **Expected Output Validation:** When running the provided test script in the editor (which performs 100 push and pop operations), calling `get_counter()` at the end must output exactly `100`.
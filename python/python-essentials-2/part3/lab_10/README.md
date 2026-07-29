## 📖 User Story: LAB 10 - Queue (FIFO)

**As a** Python student preparing for the PCAP certification,
**I want to** implement a custom `Queue` class based on the FIFO (First In, First Out) model,
**So that** I can improve my skills in defining classes from scratch, managing internal data structures, and creating custom exceptions.

---

#### ✅ Acceptance Criteria (BDD)

**Scenario 1: Initializing the Queue**
* **Given** a new instance of the `Queue` class is instantiated,
* **When** the constructor (`__init__`) is executed,
* **Then** it must initialize a hidden internal list to act as the storage for the queue elements.

**Scenario 2: Adding elements to the Queue (put)**
* **Given** an active `Queue` instance,
* **When** the `put(element)` method is called with a new element,
* **Then** the element must be inserted at the **beginning** of the internal list.

**Scenario 3: Retrieving elements from the Queue (get)**
* **Given** a `Queue` instance containing at least one element,
* **When** the `get()` method is called,
* **Then** it must remove and return the element from the **end** of the internal list (ensuring the oldest element is retrieved first).

**Scenario 4: Handling empty queue errors**
* **Given** a `Queue` instance that is empty,
* **When** the `get()` method is called,
* **Then** a custom exception named `QueueError` must be explicitly raised.

---

#### ⚙️ Technical & Business Rules

1. **Custom Exception:** A new class named `QueueError` must be defined. It should derive from a standard Python exception (e.g., `IndexError` or the base `Exception` class).
2. **Data Structure:** The core storage must be a standard Python `list`.
3. **FIFO Architecture:** The queue must strictly follow the First-In, First-Out rule (like a line in a post office). 
4. **Expected Output Validation:** When running the provided test code (which puts values `1`, `"dog"`, and `False`, and then attempts to get four times), the script must output:
   `1`
   `dog`
   `False`
   And gracefully terminate by catching the `QueueError` (printing `Queue error`).
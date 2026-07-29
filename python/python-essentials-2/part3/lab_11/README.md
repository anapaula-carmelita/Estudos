### 📖 User Story: LAB 11 - Queue (FIFO) Part 2

**As a** Python student preparing for the PCAP certification,
**I want to** extend my existing `Queue` class by creating a subclass (e.g., `SuperQueue`) that includes a new parameterless method to check if the queue is empty,
**So that** I can practice class inheritance, method extension, and state evaluation without modifying the original base class.

---

#### ✅ Acceptance Criteria (BDD)

**Scenario 1: Inheriting from the base Queue**
* **Given** a new instance of the subclass `SuperQueue` is instantiated,
* **When** the constructor (`__init__`) is executed,
* **Then** it must properly invoke the superclass (`Queue`) constructor to ensure the internal storage list is initialized.

**Scenario 2: Verifying an empty queue**
* **Given** a `SuperQueue` instance that currently has no elements,
* **When** the `isempty()` method is called,
* **Then** it must return the boolean value `True`.

**Scenario 3: Verifying a non-empty queue**
* **Given** a `SuperQueue` instance that has at least one element added via the `put()` method,
* **When** the `isempty()` method is called,
* **Then** it must return the boolean value `False`.

**Scenario 4: Preserving base class behavior**
* **Given** an active `SuperQueue` instance,
* **When** the inherited methods `put()` and `get()` are used,
* **Then** they must function exactly as they did in the base `Queue` class (strictly FIFO), raising a `QueueError` when attempting to get from an empty queue.

---

#### ⚙️ Technical & Business Rules

1. **Inheritance:** The new class must inherit directly from the `Queue` class created in the previous lab.
2. **New Method:** A parameterless method named `isempty()` must be defined inside the subclass. It only returns a boolean (`True` or `False`).
3. **No Redundancy:** You should not rewrite the `put()` or `get()` methods in the subclass; rely entirely on inheritance.
4. **Expected Output Validation:** When running the provided test script, it should correctly evaluate and print the queue's state (empty or not) as expected by the lab's instructions.
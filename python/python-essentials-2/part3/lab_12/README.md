### 📖 User Story: Lab 12 - Timer Class

**As a** Python student preparing for the PCAP certification,
**I want to** build a `Timer` class to track and manipulate hours, minutes, and seconds,
**So that** I can practice data encapsulation, overriding magic methods for string representation, and implementing state-changing methods.

---

#### ✅ Acceptance Criteria (BDD)

**Scenario 1: Initializing the Timer with encapsulation**
* **Given** a new instance of the `Timer` class is created,
* **When** the constructor (`__init__`) is executed with or without arguments (hours, minutes, seconds),
* **Then** it must initialize private properties for hours, minutes, and seconds, defaulting to `0` if no arguments are provided.

**Scenario 2: String representation (Printing the object)**
* **Given** a `Timer` object with a specific internal time,
* **When** the object is printed or converted to a string,
* **Then** it must implicitly invoke the `__str__` method,
* **And** return the time formatted strictly as `hh:mm:ss` (e.g., `09:05:03`), utilizing a standalone helper function (not a class method) to add leading zeros.

**Scenario 3: Incrementing the time (next_second)**
* **Given** an active `Timer` instance,
* **When** the `next_second()` method is called,
* **Then** the internal time must increase by exactly 1 second,
* **And** correctly roll over minutes and hours if necessary (e.g., incrementing `23:59:59` must result in `00:00:00`).

**Scenario 4: Decrementing the time (previous_second)**
* **Given** an active `Timer` instance,
* **When** the `previous_second()` method is called,
* **Then** the internal time must decrease by exactly 1 second,
* **And** correctly roll back minutes and hours if necessary (e.g., decrementing `00:00:00` must result in `23:59:59`).

---

#### ⚙️ Technical & Business Rules

1. **Encapsulation:** All class properties (hours, minutes, seconds) must be strictly private (e.g., `__hours`).
2. **Helper Function:** The string formatting logic (padding single digits with a zero) must be handled by a separate, standalone function defined outside the class, NOT a method.
3. **No Validation Required:** For this specific scope, assume the inputs provided to the constructor are always valid (hours 0-23, minutes/seconds 0-59).
4. **Expected Output Validation:** Running the provided test code should print exactly:
   `23:59:59`
   `00:00:00`
   `23:59:59`
## 📖 User Story: LAB 13 - Days of the Week (Weeker Class)

**As a** Python student preparing for the PCAP certification,
**I want to** implement a `Weeker` class capable of storing and manipulating the days of the week,
**So that** I can practice data encapsulation, custom exception handling, magic methods, and modular arithmetic for cyclic data.

---

#### ✅ Acceptance Criteria (BDD)

**Scenario 1: Initializing with a valid day**
* **Given** a new instance of the `Weeker` class is instantiated,
* **When** the constructor (`__init__`) is passed a valid day string (e.g., "Mon", "Tue"),
* **Then** it must store this day in a strictly private instance variable.

**Scenario 2: Handling invalid days with a Custom Exception**
* **Given** a new instance of the `Weeker` class is instantiated,
* **When** the constructor receives a string outside the allowed set of days,
* **Then** a custom exception named `WeekDayError` must be explicitly raised.

**Scenario 3: String representation (Printing the object)**
* **Given** an active `Weeker` object,
* **When** the object is printed or implicitly converted to a string,
* **Then** it must invoke the `__str__` method and return the currently stored day as a string (e.g., "Mon").

**Scenario 4: Adding days to the current date**
* **Given** an active `Weeker` object,
* **When** the `add_days(n)` method is called with an integer `n`,
* **Then** the internal day must roll forward exactly `n` days, wrapping around the week correctly (e.g., adding 3 days to "Fri" results in "Mon").

**Scenario 5: Subtracting days from the current date**
* **Given** an active `Weeker` object,
* **When** the `subtract_days(n)` method is called with an integer `n`,
* **Then** the internal day must roll backward exactly `n` days, wrapping around the week correctly (e.g., subtracting 2 days from "Tue" results in "Sun").

---

#### ⚙️ Technical & Business Rules

1. **Encapsulation:** All object properties must be strictly private (using double underscores, e.g., `__current_day`).
2. **Valid Days Set:** The only acceptable values for initialization are: `['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']`.
3. **Custom Exception:** The `WeekDayError` class must be defined by the developer (typically inheriting from `Exception` or `ValueError`).
4. **Expected Output Validation:** When running the provided test script, the output must be:
   `Mon`
   `Tue`
   `Sun`
   `Sorry, I can't serve your request.`
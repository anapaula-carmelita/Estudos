## 📖 User Story: LAB 15 - Triangle

**As a** Python student preparing for the PCAP certification,
**I want to** implement a `Triangle` class that embeds three `Point` class objects using composition,
**So that** I can practice object composition, manage private internal collections, and compute geometric metrics like the perimeter.

---

#### ✅ Acceptance Criteria (BDD)

**Scenario 1: Initializing the Triangle via Composition**
* **Given** three valid instances of the `Point` class,
* **When** a new instance of the `Triangle` class is created passing these three points to the constructor (`__init__`),
* **Then** the points must be stored inside the object as a private list (e.g., `__points`).

**Scenario 2: Calculating the Triangle Perimeter**
* **Given** a `Triangle` instance initialized with three coordinate points,
* **When** the parameterless `perimeter()` method is called,
* **Then** it must calculate the sum of all three side lengths (legs) of the triangle,
* **And** return the exact total perimeter as a floating-point number.

**Scenario 3: Leveraging Point distance methods**
* **Given** that the `Point` class provides distance calculation methods (such as `distance_from_point()`),
* **When** the `perimeter()` method computes the sides,
* **Then** it must utilize these methods to measure the distances between point 1 and 2, point 2 and 3, and point 3 and 1 respectively.

---

#### ⚙️ Technical & Business Rules

1. **Composition:** The `Triangle` class must not duplicate coordinate logic; it must entirely rely on embedding `Point` objects.
2. **Encapsulation:** The list containing the three points must be strictly private inside the `Triangle` instance.
3. **Parameterless Method:** The `perimeter()` method receives no extra arguments (only `self`).
4. **Expected Output Validation:** When running the provided test script in the Edube editor (with points like `(0, 0)`, `(1, 0)`, and `(0, 1)`), the evaluated perimeter must match the expected output precisely (`3.414213562373095`).
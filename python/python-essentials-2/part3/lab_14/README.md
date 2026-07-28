## 📖 User Story: LAB 14 - The Points on a plane

**As a** Python student preparing for the PCAP certification,
**I want to** implement a `Point` class representing coordinates on a Cartesian plane with support for private attributes and distance calculations,
**So that** I can practice object-oriented design, encapsulation, and coordinate geometry using Python's math module.

---

#### ✅ Acceptance Criteria (BDD)

**Scenario 1: Initializing the Point with default values**
* **Given** a request to create a new point,
* **When** the `Point` class constructor (`__init__`) is executed with or without arguments (`x` and `y`),
* **Then** it must store both coordinates as floats, defaulting both to `0.0` if no parameters are supplied,
* **And** ensure the properties are strictly private.

**Scenario 2: Accessing private coordinates via getters**
* **Given** an active `Point` instance with hidden coordinates,
* **When** the parameterless methods `getx()` and `gety()` are called,
* **Then** they must safely return the private `x` and `y` values respectively.

**Scenario 3: Calculating distance from raw coordinates (distance_from_xy)**
* **Given** an initialized `Point` object,
* **When** the `distance_from_xy(x, y)` method is called with another coordinate pair,
* **Then** it must calculate and return the Euclidean distance between the current point and the target coordinates using `math.hypot()`.

**Scenario 4: Calculating distance from another Point object (distance_from_point)**
* **Given** an initialized `Point` object,
* **When** the `distance_from_point(point)` method is called passing another `Point` instance,
* **Then** it must extract the coordinates of the target object using its getters, and return the correct Euclidean distance.

---

#### ⚙️ Technical & Business Rules

1. **Encapsulation:** The coordinates `x` and `y` must be private (e.g., `self.__x` and `self.__y`).
2. **Math Module Integration:** Use `math.hypot(dx, dy)` to compute the length of the hypotenuse (distance).
3. **Object Collaboration:** The method `distance_from_point` should ideally leverage `getx()` and `gety()` from the passed object to promote good software engineering practices.
4. **Expected Output Validation:** When running the test code provided by the lab (instantiating points and calling distance methods), it must output:
   `1.4142135623730951`
   `1.4142135623730951`
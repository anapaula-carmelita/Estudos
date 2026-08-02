# [Lab 22] - Counting Weekdays in a Year

## 📝 User Story

**As a** Python student / developer,
**I want to** create a `MyCalendar` class that extends the built-in `Calendar` class and adds a method called `count_weekday_in_year(year, weekday)`,
**So that** I can easily calculate and return the total number of times a specific day of the week occurs within a given year.

---

## ✅ Acceptance Criteria

**Scenario: Counting Mondays in a standard year**
* **Given** a year parameter of 2019 and a weekday parameter of 0 (representing Monday)
* **When** the `count_weekday_in_year(2019, 0)` method is executed
* **Then** the method must return the integer `52`.

**Scenario: Counting Sundays in a leap year**
* **Given** a year parameter of 2000 and a weekday parameter of 6 (representing Sunday)
* **When** the `count_weekday_in_year(2000, 6)` method is executed
* **Then** the method must return the integer `53`.

**Scenario: Correctly extending and utilizing the Calendar class**
* **Given** the implementation of the `MyCalendar` class
* **When** the counting method processes the weeks and days
* **Then** it must explicitly inherit from the `calendar.Calendar` base class and use its `monthdays2calendar` method to retrieve the weeks and days for the counting logic.

---

## 🛠️ Technical Notes

* **Implementation Details:** * Import the standard `calendar` module.
  * Define `class MyCalendar(calendar.Calendar):`.
  * The `monthdays2calendar(year, month)` method returns a list of weeks; each week is a list of tuples containing `(day_of_month, weekday)`. Keep in mind that `day_of_month` is `0` if the day belongs to the previous or next month.
  * You will need a nested loop structure: iterate through all 12 months, then through the weeks of each month, and finally through the days of each week. Increment a counter if the `day_of_month` is not `0` and the `weekday` matches the target parameter.
* **Complexity:** 
  * **Time:** O(1). Although there are nested loops, they always iterate a constant number of times (12 months, ~5 weeks per month, 7 days per week), independent of the input size.
  * **Space:** O(1), as you only need a single integer counter to keep track of the occurrences.
* **Dependencies:** The built-in Python `calendar` module.
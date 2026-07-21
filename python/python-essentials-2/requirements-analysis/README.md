# 🗺️ Requirements & Agile Planning Overview

This document explains the Agile methodology applied to structure the learning journey for the **Python Essentials 2** labs. 

Instead of simply writing scripts, I treated the course curriculum as a software product, utilizing **User Story Mapping** and **[Kanban Sprints](https://github.com/users/anapaula-carmelita/projects/1/views/8)** to manage deliveries.

## 🏗️ The Hierarchy (Taxonomy)

The project is structured using standard Agile taxonomy to break down the complexity of the course into manageable, deliverable increments.

### 1. The Epic: Python Essentials 2 Labs
* **Goal:** Attain practical mastery of advanced Python concepts required for the **PCAP Certification**.
* **Scope:** All theoretical modules and practical laboratories within the Python Essentials 2 curriculum.

### 2. Features (The Backbone)
The Epic is divided into four main Features (represented by the **dark green blocks** in the User Story Map). These act as the major milestones of the learning journey:
* **Feature 1:** Part 1 - Modules, Packages, and PIP. Project structure and planning sprints.
* **Feature 2:** Part 2 - Strings, String and List Methods, Exceptions.
* **Feature 3:** Part 3 - Object-Oriented Programming (OOP) - *The core of the curriculum.*
* **Feature 4:** Part 4 - Miscellaneous (File I/O, OS, Datetime, Calendar).

### 3. User Stories (The Deliverables)
Each Feature is broken down into specific User Stories, which are the actual programming labs (represented by the **light green blocks**). 
* Each User Story acts as a standalone requirement.
* Before coding, each story receives its own documentation detailing the **Business Logic** and **Acceptance Criteria**.

## 🔄 Execution: GitHub Projects & Sprints

To bring the User Story Map to life, execution is managed via a **Kanban Board on GitHub Projects**.

1. **Backlog:** All labs (User Stories) start in the general backlog.
2. **Sprints:** Stories are grouped into thematic Sprints based on their parent Feature (Sprints). 
3. **Workflow:** Tasks transition from *To Do* ➔ *In Progress* ➔ *Done* as the code is written, tested, and pushed to the repository.

This approach not only organizes the study flow but also simulates a real DevOps and Agile environment, ensuring continuous integration of knowledge.

![../assets/user-story-map.jpg](../assets/user-story-map.jpg)

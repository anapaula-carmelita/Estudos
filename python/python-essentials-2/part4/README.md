## Part 4: Miscellaneous (File I/O, OS, Datetime, Calendar).

- [x] [LAB-16 - Character Frequency Histogram](lab_16)
- [x] [LAB-17 - Sorted Character Frequency Histogram (File Output)](lab_17)
- [x] [LAB-18 - Evaluating Students' Results](lab_18)
- [x] [LAB-19 - Find a Directory!](lab_19)
- [x] [LAB-20 - Formatting Date and Time](lab_20)
- [x] [LAB-22 - Counting Weekdays in a Year](lab_22)

## 🏁 Sprint 4 Retrospective & Lessons Learned (Part 4 - Miscellaneous)

### 🎯 Sprint Goal
Complete Part 4 (Miscellaneous) of the Python Essentials curriculum, mastering file I/O, standard system modules (`os`, `datetime`, `calendar`), and elevating code quality through Agile practices, Unit Testing, and CI/CD automation.

---

### 🟢 What went well (O que funcionou bem)
- **Software Engineering in Practice:** Successfully adopted agile methodologies by writing well-structured User Stories for the labs (e.g., Histogram, Directory Search, and Calendar tasks) before jumping into the code.
- **Advanced Unit Testing & Mocks:** Implemented robust automated tests using the `unittest` framework. Mastered the use of Mocking (specifically capturing `sys.stdout`) to validate complex function outputs (like date formatting) without altering the core logic.
- **CI/CD Automation & Git Flow:** Configured GitHub Actions pipelines effectively. Establishing a professional flow of feature branching, opening Pull Requests, merging to `main`, and running automated tests reinforced core Continuous Integration principles.
- **Environment Upgrade:** Acquired a new CPU, which significantly boosted the local development environment, making script execution, local testing, and automated workflows much faster and more efficient.

---

### 🟡 Challenges & Key Learnings (Desafios e Aprendizados)
1. **Data Sorting & Lambda Functions:** - *Key takeaway:* During the Histogram lab, I learned how to efficiently sort dictionary items. Using `lambda x: x[1]` combined with `sorted()` and `reverse=True` proved to be an incredibly elegant and powerful way to sort lists of tuples in Python based on their values.
2. **Open-Source Etiquette & Portfolios:** - *Key takeaway:* Developed a "senior dev" mindset regarding software ecosystems. I realized that a well-structured GitHub repository (with release notes, actions, and tests) is the ideal way to showcase my learning progress to recruiters, deliberately choosing to keep public registries like PyPI clean from basic lab packages.
3. **Scoping the Next Steps (Certification Focus):** - *Key takeaway:* With Part 4 officially completed and the "desk clean," the immediate next step is to shift focus from guided labs to practical mock exams. The upcoming sprint will be dedicated to test-taking strategies and answering simulation questions in preparation for the PCAP-31-03 certification exam.

## ⚖️ Educational Notice

This repository contains my own implementations, tests, and technical documentation developed for educational purposes.

It is not an official Python Institute repository and does not replace the course materials. Original exercise statements are not reproduced here.

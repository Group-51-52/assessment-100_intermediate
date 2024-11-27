# **Assessment-100 Intermediate**

This repository contains a series of Python tasks designed to help students practice fundamental programming concepts. Each task is structured as a standalone module with its corresponding test file, ensuring modularity and ease of testing.

## **Project Structure**

The repository is organized as follows:

```plaintext
tasks/
├── task1_reverse_string.py       # Task 1: Reverse String
├── task2_sum_of_squares.py       # Task 2: Sum of Squares
├── task3_filter_even_numbers.py  # Task 3: Filter Even Numbers
├── task4_find_missing_number.py  # Task 4: Find Missing Number
├── task5_word_count.py           # Task 5: Word Count
tests/
├── test_task1_reverse_string.py  # Tests for Task 1
├── test_task2_sum_of_squares.py  # Tests for Task 2
├── test_task3_filter_even_numbers.py  # Tests for Task 3
├── test_task4_find_missing_number.py  # Tests for Task 4
├── test_task5_word_count.py           # Tests for Task 5

## **Getting Started**

### **Prerequisites**
To run this project and the tests, ensure you have the following installed:

- Python (version 3.8 or above)
- `pytest` (a testing framework for Python)

You can install `pytest` using pip:

```bash
pip install pytest
```

## **How to Use**

### **Solve the Tasks**
Each task file in the `tasks/` directory contains a function skeleton with a detailed docstring. Implement the logic for each function following the provided instructions.

### **Test the Solutions**
For each task, there is a corresponding test file in the `tests/` directory. These test files validate the correctness of your solution.

## **How to Run Tests**

### **Run All Tests**
To test all tasks at once, navigate to the project root directory and run:
```bash
pytest tests/
```

## **Run Tests for a Specific Task**

### **To run tests for a specific task, use the following commands:**
```bash
pytest tests/test_task1_reverse_string.py
```

```bash
pytest tests/test_task2_sum_of_squares.py
```

```bash
pytest tests/test_task3_filter_even_numbers.py
```

```bash
pytest tests/test_task4_find_missing_number.py
```

```bash
pytest tests/test_task5_word_count.py
```
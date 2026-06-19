# 📦 Amazon-Inspired Product Sorting & Filtering System

[![Python](https://img.shields.github.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.github.io/badge/Pandas-2.0%2B-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![CLI](https://img.shields.github.io/badge/Interface-CLI-lightgrey?style=for-the-badge)](https://en.wikipedia.org/wiki/Command-line_interface)

An elegant command-line interface (CLI) application that simulates **Amazon's search-refinement backend**. It enables users to load product catalogs, filter items dynamically by categories or price ranges, and sort them by price or ratings in ascending/descending order.

This was developed as an **engineering first project**, serving as an introduction to data manipulation with Python and Pandas, data persistence via JSON, and structured system demonstration.

---

## ✨ Core Features

*   **File-Based Data Persistence**: Loads product records (IDs, names, prices, ratings, and categories) directly from a local `products.json` file.
*   **Dynamic DataFrames**: Utilizes **Pandas DataFrames** to handle catalog parsing, mapping, sorting, and subsetting on the fly.
*   **E-Commerce Sort Routines**:
    *   Sort by **Price** (Ascending for "Budget-friendly", Descending for "Premium first").
    *   Sort by **Average Customer Rating** (Descending for "Top Rated").
*   **Granular Filters**:
    *   **Price Range Gating**: Restricts catalog to custom minimum and maximum price boundaries.
    *   **Category Filter**: Groups and filters items by matching categories (e.g., *Electronics*, *Home*, *Kitchen*).
*   **Session Management**: Keeps track of current filters and allows users to chain operations or perform a quick reset back to the full dataset.

---

## 🛠️ Technology Stack
*   **Language**: Python 3.x
*   **Data Structures**: JSON (JavaScript Object Notation) for product catalog storage.
*   **Libraries**:
    *   `pandas` (Engine for sorting, logical indexing, and tabular layout output).
    *   `json` (Python standard library for deserializing datasets).

---

## 📂 Project Structure
```markdown
product-sorting-system/
│
├── Product Sorting Project/
│   ├── data_handler.py      # I/O functions to read/write JSON files
│   ├── product_manager.py   # Business logic (Pandas DataFrame filters & sorting)
│   ├── main.py              # Main terminal loop, menu prompts, and system run
│   └── products.json        # Database containing 30 initial product items
│
└── README.md                # Project documentation & Viva prep guide
```

---

## 🚀 How to Run the System

### 1. Install Dependencies
This project requires the `pandas` library. Install it using `pip`:
```bash
pip install pandas
```

### 2. Launch the Application
Run the main script from your terminal:
```bash
cd "Product Sorting Project"
python main.py
```

---

## 🎓 Faculty Demo & Viva Preparation Guide
This project is an excellent tool for learning how to demonstrate technical concepts to evaluators. Below is a structured guide to help prepare for project demos and answer common examiner questions.

### 💡 1. Key Talking Points for a Perfect Demo
*   **The Problem Statement**: Explain how e-commerce platforms like Amazon handle massive volumes of product data. Highlight that manual nested loops in Python are slow, which is why you chose **Pandas** (built on optimized C-arrays) for fast operations.
*   **The User Flow**: Show a chained scenario to the examiners. E.g., *"Let's first filter for 'Kitchen' items, then narrow down to a budget of 50–150, and finally sort by highest customer rating first."* This proves your system handles combined query states.
*   **The Separation of Concerns**: Explain your modular architecture: `data_handler.py` handles I/O, `product_manager.py` handles business logic, and `main.py` runs the UI.

### ❓ 2. Common Viva/Defense Questions & Sample Answers

#### **Q1: Why did you use Pandas instead of writing custom sorting algorithms (like Bubble Sort or Quick Sort) in Python?**
> **Answer:** Writing custom sorting loops in pure Python has an overhead due to dynamic typing and interpreter loops. Pandas uses highly optimized compiled C code underneath (leveraging NumPy arrays) and implements the **Timsort** algorithm. This allows us to sort thousands of items in milliseconds, matching the performance requirements of commercial databases.

#### **Q2: What is the time complexity of the sorting operation in your program?**
> **Answer:** The sorting is handled by Pandas' `sort_values()` function, which uses Python's Timsort under the hood. The worst-case time complexity is $\mathcal{O}(n \log n)$, and the space complexity is $\mathcal{O}(n)$, which is highly efficient for data sorting.

#### **Q3: How does your price range filter work behind the scenes?**
> **Answer:** It uses **Boolean Indexing** in Pandas. By executing `df[(df["price"] >= min_price) & (df["price"] <= max_price)]`, Pandas creates a boolean mask (True/False values) for each row and retrieves only those rows where both conditions evaluate to `True`. This is done in vector space, making it much faster than standard `for` loops.

#### **Q4: What happens if the `products.json` file is missing or corrupted? How would you handle it?**
> **Answer:** In a production environment, we should wrap the file read operations in a `try-except` block. Specifically, catching `FileNotFoundError` (for missing files) and `json.JSONDecodeError` (for corrupted files) to print a clean error message and load an empty template rather than crashing the program.

---
*Created as a milestone engineering project. Demonstrating the power of clean sorting logic in terminal applications.*

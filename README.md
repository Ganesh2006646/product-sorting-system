# Amazon-Style Product Sorting System 📦

<p align="center">
  <img src="https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&w=1200&h=400&q=80" alt="Product Sorting Banner" width="100%" style="border-radius: 10px; box-shadow: 0 4px 20px rgba(0,0,0,0.15);"/>
</p>

## 📖 Story
Developed as our **engineering first project**, the **Product Sorting System** was our introduction to data management and command-line application workflows in Python. The goal was to replicate an Amazon-like product search refinement mechanism, allowing users to filter and sort catalogs dynamically.

This project gave us incredible hands-on experience in presenting our work to faculty, learning how to structure technical explanations, demonstrating running CLI loops, and resolving questions regarding sorting algorithms and computational complexities.

---

## ⚡ Features
*   **Persistent Data Storage**: Product details (price, rating, and category) are kept in a local `products.json` file.
*   **Pandas-Backed Engine**: Converts JSON data into a Pandas DataFrame for highly efficient sorting and filtering operations.
*   **Dual-Criteria Sorting**: Supports sorting items by price (ascending/descending) or average customer rating (descending).
*   **Price Gating**: Filters products within a user-defined price range.
*   **Category Filter**: Narrows the product catalog down to specific categories (e.g., Electronics, Home, Kitchen).
*   **Session Management**: Users can chain multiple sorting and filtering actions together, or reset the DataFrame back to its original state.

---

## 🛠️ Tech Stack
*   **Programming Language**: Python 3.x
*   **Data Manipulation**: Pandas
*   **Data Storage**: JSON

---

## 🚀 How to Run

### Prerequisites
*   Python 3.x installed.
*   The `pandas` library. Install it using:
    ```bash
    pip install pandas
    ```

### Steps
1. Clone this repository locally:
   ```bash
   git clone https://github.com/Ganesh2006646/product-sorting-system.git
   cd "product-sorting-system/Product Sorting Project"
   ```
2. Run the application:
   ```bash
   python main.py
   ```

---

## 🎯 Conclusion
This project laid the foundation for our engineering path, demonstrating how raw data files can be turned into structured, queryable data frames in python. Beyond the code, presenting the system to our faculty helped us build confidence in defending our technical decisions, explaining algorithm choices, and demonstrating clean terminal applications.

---

<div align="center">
  <sub>Developed with 💖 by</sub>
  <br/>
  <b><a href="https://github.com/Ganesh2006646">K Ganesh Giridhar</a></b>
  <br/>
  <sub>Amrita Vishwa Vidyapeetham</sub>
</div>

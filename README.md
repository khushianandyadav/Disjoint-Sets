# Disjoint Sets in Python

This repository contains Python implementations of the **Disjoint Set (Union-Find)** data structure, along with different union strategies.

## 📂 Files

- **`union_and_find.py`**  
  Basic implementation of Disjoint Sets with `find` and `union` operations.

- **`union_by_rank.py`**  
  Optimized union operation using **union by rank**.

- **`union_by_size.py`**  
  Optimized union operation using **union by size**.

## 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/disjoint-sets.git
   cd disjoint-sets
````

2. Run any of the implementations:

   ```bash
   python Disjoint\ Sets/union_by_size.py
   ```

## 📖 Concepts Covered

* Disjoint Set (Union-Find) data structure
* Path Compression in `find`
* Union by Rank
* Union by Size

## 🛠️ Requirements

* Python 3.x

No external libraries are required.

## ✨ Example Output

For `union_by_size.py`:

```
Element 0: Representative = 0
Element 1: Representative = 0
Element 2: Representative = 2
Element 3: Representative = 2
Element 4: Representative = 0
```

---

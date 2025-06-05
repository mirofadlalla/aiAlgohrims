# 🔍 Informed Search Algorithms: A* and Greedy Best-First Search

This project demonstrates two major **informed search algorithms** used in Artificial Intelligence:  
- **Greedy Best-First Search (GBFS)**
- **A\* Search**

Both use **heuristic functions** to estimate how close a node is to the goal and guide the search accordingly.

---

## 📌 Overview

| Algorithm | Uses Cost `g(n)` | Uses Heuristic `h(n)` | Complete | Optimal | Space/Time Complexity |
|-----------|------------------|------------------------|----------|---------|------------------------|
| Greedy Best-First Search (GBFS) | ❌ | ✅ | ❌ | ❌ | `O(b^d)` |
| A\* Search | ✅ | ✅ | ✅ | ✅ (if `h` is admissible) | `O(b^d)` |

---

## 🧠 Key Concepts

- `g(n)`: Cost from start to node `n`
- `h(n)`: Estimated cost from node `n` to the goal (heuristic)
- `f(n)`:
  - GBFS: `f(n) = h(n)` (fast but not always optimal)
  - A\*: `f(n) = g(n) + h(n)` (balanced and optimal)

---

## 🚀 Example Graph

Graph:
A
/
B(1) C(3)
\
D(1) G(2)
\ /
G

Heuristic:
G: 0
D: 1
B: 4
C: 2
A: 5

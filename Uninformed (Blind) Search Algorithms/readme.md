# 📘 Summary of Uninformed Search Algorithms

Uninformed (blind) search algorithms explore the state space without using any domain-specific information. Here's a concise summary comparing the most important uninformed search techniques:

| Algorithm | Complete | Optimal | Time Complexity | Space Complexity | Notes |
|-----------|----------|---------|------------------|-------------------|-------|
| **BFS (Breadth-First Search)** | ✅ Yes | ✅ Yes (unit cost) | O(b^d) | O(b^d) | Explores nodes level by level |
| **DFS (Depth-First Search)**   | ❌ No  | ❌ No             | O(b^d) | O(bd)  | May go infinitely deep in infinite spaces |
| **UCS (Uniform Cost Search)**  | ✅ Yes | ✅ Yes            | O(b^d) | O(b^d) | Expands the lowest-cost paths first |
| **DLS (Depth-Limited Search)** | ❌ No  | ❌ No             | O(b^l) | O(bl)  | DFS with a predefined depth limit `l` |
| **IDDFS (Iterative Deepening DFS)** | ✅ Yes | ✅ Yes (unit cost) | O(b^d) | O(bd)  | Combines DFS's low memory use with BFS's completeness |

> **Legend:**  
> - `b`: branching factor  
> - `d`: depth of the shallowest goal  
> - `l`: depth limit  

---

## ✅ Key Takeaways

- Use **BFS** or **IDDFS** when you need completeness and optimality (for unit cost problems).
- Use **UCS** when path costs vary and optimality is needed.
- Use **DFS/DLS** when memory is tight, and you’re okay with potentially missing the goal.
- **IDDFS** is a practical default when cost is uniform and space is a concern.

---

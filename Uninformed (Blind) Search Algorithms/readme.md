


 Summary of All Uninformed Search Algorithms:

 
Algorithm	Complete	Optimal	Time	Space	Notes
BFS	✅	✅ (unit cost)	O(b^d)	O(b^d)	Explores level by level
DFS	❌	❌	O(b^d)	O(bd)	May go infinitely deep
UCS	✅	✅	O(b^d)	O(b^d)	Expands lowest-cost nodes
DLS	❌	❌	O(b^l)	O(bl)	DFS with depth cutoff
IDDFS	✅	✅ (unit cost)	O(b^d)	O(bd)	Combines DFS + BFS benefits

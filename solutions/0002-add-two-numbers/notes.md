# 2. Add Two Numbers

**Difficulty:** Medium
**Pattern:** Linked List / Simulated Addition

## Approach
Both lists store digits in reverse order. Traverse both simultaneously,
summing digit-by-digit along with any carry, and build a new list from
the results.

## Complexity
- Time: O(max(m, n))
- Space: O(max(m, n))

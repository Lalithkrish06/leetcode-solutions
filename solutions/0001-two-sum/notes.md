# 1. Two Sum

**Difficulty:** Easy
**Pattern:** Array / HashMap (one-pass lookup)

## Approach
Walk through the array once. For each number, check if its complement
(`target - num`) has already been seen. If yes, return both indices.
Otherwise, store the current number and its index for future lookups.

## Complexity
- Time: O(n)
- Space: O(n)

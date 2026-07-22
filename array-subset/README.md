# Check if One Array is a Subset of Another

## Problem Summary

You are given two arrays:

- `a[]` (the main array)
- `b[]` (the array to check)

Your task is to determine whether **every element of `b[]` exists in `a[]`**.

If every element of `b[]` is present in `a[]`, return:

```text
true
```

Otherwise, return:

```text
false
```

---

# What is a Subset?

A subset is a collection whose elements all exist in another collection.

For example:

```
A = {1, 2, 3, 4}
B = {2, 4}
```

Since every element in `B` exists in `A`, `B` is a subset of `A`.

---

# Examples

## Example 1

### Input

```text
a[] = [11, 7, 1, 13, 21, 3, 7, 3]
b[] = [11, 3, 7, 1, 7]
```

### Output

```text
true
```

### Explanation

All elements in `b[]` exist in `a[]`.

---

## Example 2

### Input

```text
a[] = [1, 2, 3, 4, 4, 5, 6]
b[] = [1, 2, 4]
```

### Output

```text
true
```

### Explanation

The elements `1`, `2`, and `4` all exist in `a[]`.

---

## Example 3

### Input

```text
a[] = [10, 5, 2, 23, 19]
b[] = [19, 5, 3]
```

### Output

```text
false
```

### Explanation

The number `3` does not exist in `a[]`.

---

# Constraints

```text
1 ≤ a.size(), b.size() ≤ 10^5

1 ≤ a[i], b[i] ≤ 10^6
```

Because the arrays can contain up to **100,000 elements**, we should use an efficient solution.

---

---

# Complexity Analysis

Let:

```text
n = size of a
m = size of b
```

## Time Complexity

Creating the set:

```text
O(n)
```

Checking every element:

```text
O(m)
```

Overall:

```text
O(n + m)
```

---

## Space Complexity

The set stores every unique element from `a`.

```text
O(n)
```

---

# Main Concepts Learned

This problem teaches:

- Using sets for fast lookup.
- Membership checking.
- The `issubset()` method.
- Improving time complexity.

The overall pattern is:

```text
Array A
     ↓
Convert to Set
     ↓
Check every element of B
     ↓
Missing?
   ↓       ↓
 Yes      No
False    True
```

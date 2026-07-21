# List Comprehensions (Python)

Generate all possible coordinates of a 3D grid using **list comprehensions**, excluding the coordinates whose sum equals a given integer.

## 📖 Problem Statement

You are given four integers:

- `x` - maximum value of the x-coordinate
- `y` - maximum value of the y-coordinate
- `z` - maximum value of the z-coordinate
- `n` - an integer to exclude

Print a list of all possible coordinates `[i, j, k]` on a 3D grid such that:

- `0 <= i <= x`
- `0 <= j <= y`
- `0 <= k <= z`
- `i + j + k != n`

Use **Python list comprehensions** instead of multiple loops.

---

## 🎯 Task

Generate every valid coordinate of the cuboid and exclude any coordinate whose elements sum to `n`.

The output should be in **lexicographic increasing order**.

---

## 📝 Input Format

Four integers, each on a separate line:

```text
x
y
z
n
```

---

## 📤 Output Format

Print a list containing all valid coordinates.

---

## 📥 Sample Input 1

```text
1
1
1
2
```

### Sample Output 1

```text
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
```

### Explanation

All possible coordinates are:

```text
[0,0,0]
[0,0,1]
[0,1,0]
[0,1,1]
[1,0,0]
[1,0,1]
[1,1,0]
[1,1,1]
```

The coordinates whose sum equals `2` are removed:

```text
[0,1,1]
[1,0,1]
[1,1,0]
```

The remaining coordinates are printed.

---

## 📥 Sample Input 2

```text
2
2
2
2
```

### Sample Output 2

```text
[
 [0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2],
 [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1],
 [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2],
 [2, 2, 0], [2, 2, 1], [2, 2, 2]
]
```

---

## 💻 Solution

```python
def generate_coordinates(x, y, z, n):
    return [
        [i, j, k]
        for i in range(x + 1)
        for j in range(y + 1)
        for k in range(z + 1)
        if i + j + k != n
    ]


if __name__ == "__main__":
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print(generate_coordinates(x, y, z, n))
```

---

## 🧠 Concepts Used

- List Comprehensions
- Nested Iteration
- Conditional Filtering
- Python Lists

---

## ⏱️ Complexity

- **Time Complexity:** `O((x + 1)(y + 1)(z + 1))`
- **Space Complexity:** `O((x + 1)(y + 1)(z + 1))` (for storing the resulting list)

---

## 🚀 Example

### Input

```text
1
2
1
2
```

### Output

```text
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 2, 0], [0, 2, 1], [1, 0, 0], [1, 1, 1], [1, 2, 0], [1, 2, 1]]
```

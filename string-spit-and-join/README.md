# Split and Join String (Python)

A simple Python program that splits a string into words using spaces and then joins those words back together using hyphens (`-`).

## 📖 Problem Statement

In Python, a string can be split using a delimiter.

### Example

```python
a = "this is a string"
a = a.split(" ")
print(a)
```

**Output**

```python
['this', 'is', 'a', 'string']
```

Joining the list back into a string is just as simple.

```python
a = "-".join(a)
print(a)
```

**Output**

```text
this-is-a-string
```

---

## 🎯 Task

Given a string of space-separated words:

1. Split the string using a space (`" "`).
2. Join the resulting words using a hyphen (`"-"`).
3. Return the new string.

---

## 📝 Function Description

```python
split_and_join(line)
```

### Parameter

| Parameter | Type | Description |
|-----------|------|-------------|
| `line` | `str` | A string containing space-separated words |

### Returns

| Type | Description |
|------|-------------|
| `str` | The string with words joined by hyphens |

---

## 📥 Input Format

A single line containing a string of space-separated words.

### Sample Input

```text
this is a string
```

---

## 📤 Output Format

A single string with words separated by hyphens.

### Sample Output

```text
this-is-a-string
```

---

## 💻 Solution

```python
def split_and_join(line):
    return "-".join(line.split())

if __name__ == "__main__":
    line = input()
    result = split_and_join(line)
    print(result)
```

---

## 🚀 Example

**Input**

```text
hello world from python
```

**Output**

```text
hello-world-from-python
```

---

## ⏱️ Complexity

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

where `n` is the length of the input string.

---

## 🛠️ Concepts Used

- Strings
- `split()`
- `join()`
- Functions
- User Input

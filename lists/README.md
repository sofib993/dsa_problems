# HackerRank: Python Lists

## Problem Summary

You are given an empty list. You need to perform different operations on the list based on commands given as input.

The available commands are:

| Command | Description |
|---|---|
| `insert i e` | Insert integer `e` at index `i` |
| `print` | Print the list |
| `remove e` | Remove the first occurrence of integer `e` |
| `append e` | Add integer `e` to the end of the list |
| `sort` | Sort the list in ascending order |
| `pop` | Remove the last element |
| `reverse` | Reverse the list |

---

## Input Format

The first line contains an integer `N`, representing the number of commands.

The next `N` lines contain commands.

Example:

```
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
```

---

# Understanding the Input

The first line:

```python
N = int(input())
```

reads the number of commands.

Example:

```
12
```

means:

```python
N = 12
```

There are 12 operations to perform.

---

## Reading Each Command

We use a loop because we need to read `N` commands:

```python
for _ in range(N):
    command = input().split()
```

Example input:

```
insert 0 5
```

After splitting:

```python
command = ["insert", "0", "5"]
```

Now:

```python
command[0] = "insert"
command[1] = "0"
command[2] = "5"
```

We use `command[0]` to know which operation to perform.

---

# Important Python List Methods

## Insert

Syntax:

```python
list.insert(index, value)
```

Example:

```python
arr = [1, 3]

arr.insert(1, 2)

print(arr)
```

Output:

```
[1, 2, 3]
```

---

## Append

Adds an element to the end.

```python
arr.append(5)
```

Example:

```
[1, 2, 3]
```

becomes:

```
[1, 2, 3, 5]
```

---

## Remove

Removes the first occurrence.

```python
arr.remove(3)
```

Example:

```
[1, 3, 3, 5]
```

becomes:

```
[1, 3, 5]
```

---

## Sort

```python
arr.sort()
```

Example:

```
[5,2,8,1]
```

becomes:

```
[1,2,5,8]
```

---

## Pop

Removes the last element.

```python
arr.pop()
```

Example:

```
[1,2,3]
```

becomes:

```
[1,2]
```

---

## Reverse

```python
arr.reverse()
```

Example:

```
[1,2,3]
```

becomes:

```
[3,2,1]
```

---

# Mistakes I made

## Mistake 1: Processing commands outside the loop

Wrong:

```python
for _ in range(N):
    command = input()

# command processing here
```

This only processes the **last command**.

Correct:

```python
for _ in range(N):
    command = input().split()

    # process command here
```

---

## Mistake 2: Creating a nested list accidentally

Wrong:

```python
cs = []
cs.append(command.split())
```

Result:

```python
[['insert', '0', '5']]
```

Correct:

```python
cs = command.split()
```

Result:

```python
['insert', '0', '5']
```

---

# Main Concept Learned

This problem teaches:

1. Reading multiple inputs using loops.
2. Parsing strings using `.split()`.
3. Using list methods.
4. Using conditions to execute different actions.

The general pattern:

```
Read command
      ↓
Split command into parts
      ↓
Check command type
      ↓
Perform operation
      ↓
Repeat
```

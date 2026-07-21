# Nested Lists (Python)

Given the names and grades of students in a class, store the data in a nested list and print the name(s) of the student(s) with the **second lowest grade**.

If multiple students have the second lowest grade, print their names in **alphabetical order**, one per line.

---

## 📖 Problem Statement

You are given the names and grades of `N` students.

Your task is to:

1. Store each student's information as a nested list in the form:
   ```python
   [name, grade]
   ```
2. Find the **second lowest unique grade**.
3. Print the name(s) of all students who have that grade.
4. If there are multiple students with the second lowest grade, print their names in alphabetical order.

---

## 📝 Input Format

- The first line contains an integer `N`, the number of students.
- The next `N` pairs of lines contain:
  - A student's name.
  - Their grade (floating-point number).

---

## 📤 Output Format

Print the name(s) of the student(s) with the second lowest grade.

If multiple students have the same second lowest grade, print each name on a new line in alphabetical order.

---

## 📥 Sample Input

```text
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
```

### Sample Output

```text
Berry
Harry
```

---

## 💡 Explanation

The nested list becomes:

```python
students = [
    ['Harry', 37.21],
    ['Berry', 37.21],
    ['Tina', 37.2],
    ['Akriti', 41],
    ['Harsh', 39]
]
```

The unique grades are:

```text
37.2
37.21
39
41
```

- Lowest grade = **37.2**
- Second lowest grade = **37.21**

The students with that grade are:

- Berry
- Harry

After sorting alphabetically:

```text
Berry
Harry
```

---

## 💻 Solution

```python
if __name__ == "__main__":
    students = []

    for _ in range(int(input())):
        name = input()
        grade = float(input())
        students.append([name, grade])

    grades = sorted(set(student[1] for student in students))
    second_lowest = grades[1]

    names = sorted(
        student[0]
        for student in students
        if student[1] == second_lowest
    )

    for name in names:
        print(name)
```

---

## 🧠 Concepts Used

- Nested Lists
- Lists
- Sets
- Sorting
- List Comprehensions
- Loops

---

## ⏱️ Complexity

- **Time Complexity:** `O(n log n)`
- **Space Complexity:** `O(n)`

where `n` is the number of students.

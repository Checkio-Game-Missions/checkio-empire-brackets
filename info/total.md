Correct orders are most important part of victory.
But sometimes redundant or missing bracket can change whole algorithm.
We should be prepared.

You are given an expression with numbers, brackets and operators.
For this task only the brackets matter. Brackets come in three flavors: "{}" "()" or "[]".
Brackets are used to determine scope or to restrict some expression. 
If a bracket is open, then it must be closed with a closing bracket of the same type. 
The scope of a bracket must not intersected by another bracket. 
For this task, you should to make a decision to correct an expression or not based on the brackets. 
Do not worry about operators and operands.

**Input:** An expression with different of types brackets as a string 

**Output:** A verdict on the correctness of the expression in boolean (True or False).

**Example:**

```python
check_brackets("((5+3)*2+1)") == True
check_brackets("{[(3+1)+2]+}") == True
check_brackets("(3+{1-1)}") == False
check_brackets("[1+1]+(2*2)-{3/3}") == True
check_brackets("(({[(((1)-2)+3)-3]/3}-3)") == False
check_brackets("2+3") == True
```
**How it is used:**

When you write code or complex expressions in a mathematical package,
you can get a huge headache when it comes to excess or missing brackets.
This concept can be useful for your own IDE.

**Precondition:**
There are only brackets ("{}" "()" or "[]"), digits or operators ("+" "-" "*" "/").<br>

```python
0 < len(expression) < 1000
```


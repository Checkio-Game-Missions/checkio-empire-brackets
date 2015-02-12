**Example:**

```python
check_brackets("((5+3)*2+1)") == True
check_brackets("{[(3+1)+2]+}") == True
check_brackets("(3+{1-1)}") == False
check_brackets("[1+1]+(2*2)-{3/3}") == True
check_brackets("(({[(((1)-2)+3)-3]/3}-3)") == False
check_brackets("2+3") == True
```
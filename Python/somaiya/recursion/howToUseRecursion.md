# Recursion

**What is Recursion?**

Recursion is used to call a block of code infinite times till
you meet your end result.

i.e To create such a function which has itself in it.
here is an example of the same: 

**Code:**

```
def a(n):
  return a(n) + a(n-1)

```

**Steps to recurse:**
1. Base case: which means when to stop. 
2. Recurse case: things to recurse.


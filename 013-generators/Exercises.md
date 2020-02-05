- Write a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
```python
    def putNumbers(n):
        i = 0
        while i<n:
            j=i
            i=i+1
            if j%7==0:
                yield j
```

def f():
    yield from "Python"


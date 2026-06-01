# 1. Add 5 to every element in nested list
lst = [[1, 2], [3, 4], [5, 6]]
result = list(map(lambda x: list(map(lambda y: y + 5, x)), lst))
print(result)

# 2. Filter dictionary values greater than 50
d = {"apple": 100, "banana": 40, "cherry": 150}
result = dict(filter(lambda x: x[1] > 50, d.items()))
print(result)

# 3. Find largest element using reduce
from functools import reduce

lst = list(map(int, input("Enter numbers: ").split()))
largest = reduce(lambda a, b: a if a > b else b, lst)
print("Largest:", largest)

# 4. What happens if reduce lambda has wrong number of parameters?

from functools import reduce

lst = [1, 2, 3]

# One parameter
# reduce(lambda x: x + 1, lst)
# Output: TypeError

# Three parameters
# reduce(lambda x, y, z: x + y + z, lst)
# Output: TypeError

# Reason:
# reduce() always passes exactly 2 arguments at a time.

# 5. Convert string characters to ASCII values
s = "Python"
result = list(map(lambda x: ord(x), s))
print(result)

# 6. Remove vowels using filter
s = "Programming"
result = "".join(filter(lambda x: x.lower() not in "aeiou", s))
print(result)

# 7. Combine list of characters into string using reduce
from functools import reduce

lst = ['P', 'y', 't', 'h', 'o', 'n']
result = reduce(lambda a, b: a + b, lst)
print(result)

# 8. Get memory addresses of list elements
lst = [10, 350, 10, 350, 20]
result = list(map(id, lst))
print(result)

# Same values may share same memory address because Python reuses objects.

# 9. Difference between map(str, lst) and map(lambda x: str(x), lst)

lst = [1, 2, 3]

print(list(map(str, lst)))
print(list(map(lambda x: str(x), lst)))

# map(str, lst) is faster because it directly uses built-in str().

# 10. Square numbers, keep multiples of 5, then find sum
from functools import reduce

lst = [5, 10, 15, 20, 25, 30]

result = reduce(
    lambda a, b: a + b,
    filter(
        lambda x: x % 5 == 0,
        map(lambda x: x ** 2, lst)
    )
)
print(result)


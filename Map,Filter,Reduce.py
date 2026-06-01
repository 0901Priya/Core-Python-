#2. Using map() with two lists
a = [1, 2, 3, 4]
b = [10, 20, 30, 40]
result = list(map(lambda x, y: x + y, a, b))
print(result)

#If lists have unequal length:
a = [1, 2, 3]
b = [10, 20, 30, 40]
result = list(map(lambda x, y: x + y, a, b))
print(result)
#map() stops when the shortest iterable is exhausted.


#3. Using filter() and lambda
nums = [12, 15, 7, 18, 20, 21, 25]
result = list(filter(
    lambda x: (x % 3 == 0 or x % 5 == 0) and not (x % 3 == 0 and x % 5 == 0),
    nums
))
print(result)

#Explanation:
#(x % 3 == 0 or x % 5 == 0)
#Checks if the number is divisible by 3 or 5.

#not (x % 3 == 0 and x % 5 == 0)
#Excludes numbers divisible by both 3 and 5.

#Examples:
#12 → divisible by 3 only ✔
#20 → divisible by 5 only ✔
#15 → divisible by both ✘


#4. Using reduce() with initial value 10
from functools import reduce
nums = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, nums, 10)
print(result)
#The initial value acts as the starting accumulator.


#5. Code Analysis
nums = [[1, 2], [3, 4], [5, 6]]
result = list(map(lambda x: x.append(10), nums))
print("Result:", result)
print("Nums:", nums)

#Reason:
#append() modifies the list in place and returns None.
#Therefore map() collects [None, None, None] while nums gets modified.

#To avoid modifying nums:

nums = [[1, 2], [3, 4], [5, 6]]
result = list(map(lambda x: x + [10], nums))
print(result)
print(nums)

#x + [10] creates a new list, so the original nums remains unchanged.




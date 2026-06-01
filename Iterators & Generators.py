# 1. Custom iterator that prints numbers from 1 to N

class Numbers:
    def __init__(self, n):
        self.n = n
        self.i = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= self.n:
            x = self.i
            self.i += 1
            return x
        raise StopIteration

print("1 to N:")
for i in Numbers(5):
    print(i)

# 2. Iterator that returns only even numbers from a list

class EvenIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.data):
            num = self.data[self.index]
            self.index += 1
            if num % 2 == 0:
                return num
        raise StopIteration

print("\nEven Numbers:")
for i in EvenIterator([1, 2, 3, 4, 5, 6]):
    print(i)

# 3. Iterator that prints string in reverse order

class ReverseString:
    def __init__(self, s):
        self.s = s
        self.index = len(s) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= 0:
            ch = self.s[self.index]
            self.index -= 1
            return ch
        raise StopIteration

print("\nReverse String:")
for i in ReverseString("Python"):
    print(i)

# 4. Iterator that yields index and element

class IndexIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = (self.index, self.data[self.index])
            self.index += 1
            return result
        raise StopIteration

print("\nIndex and Element:")
for i in IndexIterator(['a', 'b', 'c']):
    print(i)

# 5. Generator that yields digits from an integer

def digits(n):
    for i in str(n):
        yield i

print("\nDigits:")
for i in digits(12345):
    print(i)

# 6. Generator for cumulative sum

def cumulative_sum(lst):
    total = 0
    for i in lst:
        total += i
        yield total

print("\nCumulative Sum:")
for i in cumulative_sum([1, 2, 3, 4]):
    print(i)

# 7. Generator that yields vowels from a string

def vowels(s):
    for i in s:
        if i.lower() in "aeiou":
            yield i

print("\nVowels:")
for i in vowels("Education"):
    print(i)

# 8. Iterator that yields words from a sentence

class WordIterator:
    def __init__(self, sentence):
        self.words = sentence.split()
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.words):
            word = self.words[self.index]
            self.index += 1
            return word
        raise StopIteration

print("\nWords:")
for i in WordIterator("Python is easy"):
    print(i)

# 9. Iterator that returns characters at even indices

class EvenIndex:
    def __init__(self, s):
        self.s = s
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.s):
            ch = self.s[self.index]
            self.index += 2
            return ch
        raise StopIteration

print("\nCharacters at Even Indices:")
for i in EvenIndex("Python"):
    print(i)

# 10. Generator that yields running maximum

def running_max(lst):
    m = lst[0]
    for i in lst:
        if i > m:
            m = i
        yield m

print("\nRunning Maximum:")
for i in running_max([3, 1, 4, 2, 5]):
    print(i)
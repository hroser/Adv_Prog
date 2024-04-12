# make a list
a = ['one', 'two', 'three']
print('a:', a)        # ['one', 'two', 'three']

# NOTE: assigning a list using = will not make copy,
# but point to the same list
b = a
print('b:', b)
a[0] = 'four'
print('b:', b)

# concatenate using +
print(a + a)

# iterate through list
for x in a:
    print(x)

# test if a given element is in a list
print('a:', a)
print('five' in a)  # False
print('two' in a)   # True

# list comprehension
nums = [1, 2, 3, 4]
squares = [ n*n for n in nums]
print(squares)

# list comprehensions can also have a conditional term
nums = [1, 2, 3, 4]
squares = [ n*n for n in nums if n != 2]
print(squares)
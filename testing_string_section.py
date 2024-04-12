# formatted string
print('the number is {0}'.format(a))

# f-strings
print(f'the number is {a}')

# integer divison
print(10 // 6)      # 1

# remainder/modulo division
print(10 % 6)       # 4

# power operation
print(2**4)         # 2^4 = 16

# test the isdigit function
s = 'hello'
print('s:', s)
print(s.isdigit())      # False
s = '22'
print('s:', s)
print(s.isdigit())      # True

# example for string splitting
s = 'ab-cd-ef'
split = s.split('-')
print(split)     # ['ab', 'cd', 'ef']

# joining string using a character
print('*'.join(split))      # ab*cd*ef

# string slicing
# return string until index -3 (excluding -3)
# witch o beeing index -1
s = 'Hello'
print(s[:-3])       # He     

# return the last two characters of a string of unknown length
s = 'abcdefgh'
print(s[-2:])
print(s[:6] + s[6:])

# formatting options
value = 2.791514
print(f'value = {value:.2f}')   # value = 2.79
print(f'value = {value:8.2f}')  # value =     2.79

# old string formatting style
text = "%d little pigs come out, or I'll %s" % (3, 'huff')      # 3 little pigs come out, or I'll huff
print(text)

# newer string formatting style
text = "{} little pigs come out, or I'll {}".format(3, 'huff')    # 3 little pigs come out, or I'll huff
print(text)

# newer string formatting style
text = "{0} little pigs {1} out, or I'll {1}".format(3, 'huff')    # 3 little pigs huff out, or I'll huff
print(text)

# newer string formatting style
text = "{0} little pigs {1} out, or I'll {0}".format(3, 'huff')    # 3 little pigs huff out, or I'll 3
print(text)

# newest string formatting style
a = '3'
s = 'huff'
text = f"{a} little pigs {s} out, or I'll {a}"   # 3 little pigs huff out, or I'll 3
print(text)

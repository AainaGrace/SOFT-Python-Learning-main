# Day 4 String

# Single line comment
letter = 'X'                # A string could be a single character or a bunch of texts
print(letter)               # X
print(len(letter))          # 1
greeting = 'Greetings, Earthlings!'  # String could be a single or double quote
print(greeting)             # Greetings, Earthlings!
print(len(greeting))        # 21
sentence = "Mastering software engineering requires persistent daily effort"
print(sentence)

# Multiline String
multiline_string = '''I enjoy designing elegant software solutions. Writing clean code makes complex systems easy to maintain. That is why I practice every single day.'''
print(multiline_string)

# Another way of doing the same thing
multiline_string = """I enjoy designing elegant software solutions. Writing clean code makes complex systems easy to maintain. That is why I practice every single day."""
print(multiline_string)

# String Concatenation
first_name = 'Ada'
last_name = 'Lovelace'
space = ' '
full_name = first_name + space + last_name
print(full_name)  # Ada Lovelace

# Checking length of a string using len() builtin function
print(len(first_name))  # 3
print(len(last_name))   # 8
print(len(first_name) > len(last_name))  # False
print(len(full_name))  # 12

# Unpacking characters
language = 'Script'
a, b, c, d, e, f = language  # unpacking sequence characters into variables
print(a)  # S
print(b)  # c
print(c)  # r
print(d)  # i
print(e)  # p
print(f)  # t

# Accessing characters in strings by index
language = 'Script'
first_letter = language[0]
print(first_letter)  # S
second_letter = language[1]
print(second_letter)  # c
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)  # t

# Negative indexing
language = 'Script'
last_letter = language[-1]
print(last_letter)  # t
second_last = language[-2]
print(second_last)  # p

# Slicing
language = 'Script'
first_three = language[0:3]
last_three = language[3:6]
print(last_three)  # ipt

# Another way
last_three = language[-3:]
print(last_three)   # ipt
last_three = language[3:]
print(last_three)   # ipt

# Skipping character while splitting Python strings
language = 'Script'
pto = language[0:6:2]
print(pto)  # Sic

# Escape sequence
print('Continuous learning opens endless professional opportunities.\nDo you agree?')  # line break
print('Phase\tTopics\tProjects')
print('Phase 1\t5\t10')
print('Phase 2\t6\t12')
print('Phase 3\t4\t8')
print('Phase 4\t7\t15')
print('This is a back slash symbol (\\)')  # To write a back slash
print('Every programmer starts with "Hello, World!"')

# String Methods

# capitalize(): Converts the first character of the string to Capital Letter
challenge = 'one hundred days of code'
print(challenge.capitalize())  # 'One hundred days of code'

# count(): returns occurrences of substring in string
challenge = 'one hundred days of code'
print(challenge.count('e'))  # 3
print(challenge.count('e', 5, 20))  # 1
print(challenge.count('de'))  # 2

# endswith(): Checks if a string ends with a specified ending
challenge = 'one hundred days of code'
print(challenge.endswith('code'))  # True
print(challenge.endswith('java'))  # False

# expandtabs(): Replaces tab character with spaces
challenge = 'one\thundred\tdays\tof\tcode'
print(challenge.expandtabs())   # 'one     hundred days    of      code'
print(challenge.expandtabs(12)) # 'one         hundred     days        of          code'

# find(): Returns the index of first occurrence of substring
challenge = 'one hundred days of code'
print(challenge.find('e'))  # 2
print(challenge.find('hundred')) # 4

# format(): formats string into nicer output
first_name = 'Ada'
last_name = 'Lovelace'
job = 'mathematician'
country = 'United Kingdom'
sentence = 'I am {} {}. I am a {}. I lived in {}.'.format(first_name, last_name, job, country)
print(sentence)  # I am Ada Lovelace. I am a mathematician. I lived in United Kingdom.

radius = 14
pi = 3.14159
area = pi * (radius ** 2)
result = 'The area of circle with radius {} is {}'.format(str(radius), str(area))
print(result)  # The area of circle with radius 14 is 615.75164

# index(): Returns the index of substring
challenge = 'one hundred days of code'
print(challenge.index('e'))  # 2
print(challenge.index('hundred')) # 4

# isalnum(): Checks alphanumeric character
challenge = 'OneHundredDaysOfCode'
print(challenge.isalnum())  # True
challenge = '100DaysOfCode'
print(challenge.isalnum())  # True
challenge = 'one hundred days of code'
print(challenge.isalnum())  # False

# isalpha(): Checks if all characters are alphabets
challenge = 'OneHundredDaysOfCode'
print(challenge.isalpha())  # True
num = '456'
print(num.isalpha())        # False

# isdigit(): Checks Digit Characters
challenge = 'Hundred'
print(challenge.isdigit())  # False
challenge = '100'
print(challenge.isdigit())  # True

# isdecimal(): Checks decimal characters
num = '50'
print(num.isdecimal())    # True
num = '50.75'
print(num.isdecimal())  # False

# isidentifier(): Checks for valid identifier (variable name)
challenge = '100DaysOfCode'
print(challenge.isidentifier())  # False (starts with a number)
challenge = 'one_hundred_days_of_code'
print(challenge.isidentifier())  # True

# islower(): Checks if all alphabets in a string are lowercase
challenge = 'one hundred days of code'
print(challenge.islower())  # True
challenge = 'One hundred days of code'
print(challenge.islower())  # False

# isupper(): Checks if all characters are uppercase
challenge = 'one hundred days of code'
print(challenge.isupper())  # False
challenge = 'ONE HUNDRED DAYS OF CODE'
print(challenge.isupper())  # True

# isnumeric(): Checks numeric characters
num = '100'
print(num.isnumeric())     # True
print('hundred'.isnumeric()) # False

# join(): Returns a concatenated string
tech_stack = ['FastAPI', 'PostgreSQL', 'Docker', 'Kubernetes']
result = ' -> '.join(tech_stack)
print(result)  # 'FastAPI -> PostgreSQL -> Docker -> Kubernetes'

# strip(): Removes leading and trailing specified characters
challenge = '  one hundred days of code  '
print(challenge.strip())  # 'one hundred days of code'

# replace(): Replaces substring inside
challenge = 'one hundred days of code'
print(challenge.replace('code', 'learning'))  # 'one hundred days of learning'

# split(): Splits String into a list
challenge = 'one hundred days of code'
print(challenge.split())  # ['one', 'hundred', 'days', 'of', 'code']

# title(): Returns a Title Cased String
challenge = 'one hundred days of code'
print(challenge.title())  # One Hundred Days Of Code

# swapcase(): Swaps uppercase to lowercase and vice versa
challenge = 'One Hundred Days Of Code'
print(challenge.swapcase())  # oNE hUNDRED dAYS oF cODE

# startswith(): Checks if String starts with the specified string
challenge = 'one hundred days of code'
print(challenge.startswith('one'))  # True
challenge = '100 days of code'
print(challenge.startswith('one'))  # False
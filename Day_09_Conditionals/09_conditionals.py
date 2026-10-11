# Level 1
# 1
age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to learn to drive.")
else:
    years_left = 18 - age
    print(f"You need {years_left} more years to learn to drive.")

#2
my_age = 25  # You can change this to your actual age
your_age = int(input("Enter your age: "))

if your_age > my_age:
    diff = your_age - my_age
    if diff == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {diff} years older than me.")
elif my_age > your_age:
    diff = my_age - your_age
    if diff == 1:
        print("I am 1 year older than you.")
    else:
        print(f"I am {diff} years older than you.")
else:
    print("We are the same age!")

#3
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")

#Level 2
#1
score = int(input("Enter student score: "))

if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score <= 89:
    print("Grade: B")
elif score >= 70 and score <= 79:
    print("Grade: C")
elif score >= 60 and score <= 69:
    print("Grade: D")
elif score >= 0 and score <= 59:
    print("Grade: F")
else:
    print("Invalid score entered!")

#2
month = input("Enter the month: ").capitalize()

if month in ['September', 'October', 'November']:
    print("The season is Autumn.")
elif month in ['December', 'January', 'February']:
    print("The season is Winter.")
elif month in ['March', 'April', 'May']:
    print("The season is Spring.")
elif month in ['June', 'July', 'August']:
    print("The season is Summer.")
else:
    print("Invalid month entered!")

#3fruits = ['banana', 'orange', 'mango', 'lemon']

new_fruit = input("Enter a fruit name: ").lower()

if new_fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(new_fruit)
    print("Updated fruit list:", fruits)

# Level 3
# 1
# The updated person dictionary
person = {
    'first_name': 'Eva',
    'last_name': 'Maria',
    'age': 18,
    'country': 'Iceland',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# 1. Check for 'skills' key and print the middle skill
if 'skills' in person:
    skills_list = person['skills']
    middle_index = len(skills_list) // 2
    print("Middle skill:", skills_list[middle_index])

# 2. Check if 'skills' exists and if 'Python' is in it
if 'skills' in person:
    if 'Python' in person['skills']:
        print("Python skill: True")
    else:
        print("Python skill: False")

# 3. Check developer title based on skills
skills = person['skills']
if 'JavaScript' in skills and 'React' in skills and len(skills) == 2:
    print('He is a front end developer')
elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
    print('He is a backend developer')
elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
    print('He is a fullstack developer')
else:
    print('unknown title')

# 4. Check marriage and country status
if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in Finland. He is married.")
else:
    print(f"{person['first_name']} {person['last_name']} does not match the marriage/country criteria.")
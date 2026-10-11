dog = {}

dog['name'] = 'Buddy'
dog['color'] = 'Brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 3

student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 20,
    'marital_status': 'Single',
    'skills': ['Python', 'HTML'],
    'country': 'USA',
    'city': 'New York',
    'address': '123 Main St'
}

print(len(student))  # Output: 9

print(student['skills'])
print(type(student['skills']))  # Output: <class 'list'>

student['skills'].append('CSS')
student['skills'].append('JavaScript')

print(list(student.keys()))

print(list(student.values()))

print(list(student.items()))

student.pop('marital_status')
# Alternatively: del student['marital_status']

del dog
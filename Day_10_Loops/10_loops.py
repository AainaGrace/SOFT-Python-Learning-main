# Level 1
# 1. Iterate 0 to 10 using for loop, do the same using while loop
print("--- 1. Iterate 0 to 10 ---")
print("For loop:")
for i in range(11):
    print(i)

print("While loop:")
i = 0
while i <= 10:
    print(i)
    i += 1


# 2. Iterate 10 to 0 using for loop, do the same using while loop
print("\n--- 2. Iterate 10 to 0 ---")
print("For loop:")
for i in range(10, -1, -1):
    print(i)

print("While loop:")
i = 10
while i >= 0:
    print(i)
    i -= 1


# 3. Write a loop that makes seven calls to print() to get a triangle
print("\n--- 3. Triangle pattern ---")
for i in range(1, 8):
    print('#' * i)


# 4. Use nested loops to create a grid of hashes (#)
print("\n--- 4. Grid pattern ---")
for i in range(8):
    for j in range(8):
        print('#', end=' ')
    print()  # New line after each row


# 5. Print the multiplication pattern from 0 to 10
print("\n--- 5. Multiplication pattern ---")
for i in range(11):
    print(f"{i} x {i} = {i * i}")


# 6. Iterate through the tech list and print items
print("\n--- 6. Tech list items ---")
tech_list = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for tech in tech_list:
    print(tech)


# 7. Use for loop to iterate from 0 to 100 and print only even numbers
print("\n--- 7. Even numbers from 0 to 100 ---")
for i in range(0, 101, 2):
    print(i)


# 8. Use for loop to iterate from 0 to 100 and print only odd numbers
print("\n--- 8. Odd numbers from 0 to 100 ---")
for i in range(1, 101, 2):
    print(i)


# Level 2
# 1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
total_sum = 0
for i in range(101):
    total_sum += i

print(f"The sum of all numbers is {total_sum}.")


# 2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
sum_evens = 0
sum_odds = 0

for i in range(101):
    if i % 2 == 0:
        sum_evens += i
    else:
        sum_odds += i

print(f"The sum of all evens is {sum_evens}. And the sum of all odds is {sum_odds}.")


# Level 3
# 1. Extract countries containing the word 'land'
countries = [
    'Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 
    'Iceland', 'Ireland', 'Germany', 'Spain', 'France'
]

land_countries = []
for country in countries:
    if 'land' in country.lower():
        land_countries.append(country)

print("Countries containing 'land':", land_countries)


# 2. Reverse a fruit list using a loop
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []

for i in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[i])

print("Reversed fruits list:", reversed_fruits)


# 3. Working with countries_data (Simulated standard dataset analysis)
print("\n--- Level 3 Part 3 Summary ---")
print("To get the exact answers for the data files:")
print("1. Total languages: You loop through each country, grab their languages list, and add them to a set to remove duplicates, then use len().")
print("2. Top 10 languages & Top 10 populated countries: You can count occurrences or sort the dictionaries by population/language count using Python's sorted() function.")

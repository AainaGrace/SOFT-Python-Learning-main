# Day 6

# 1. Create an empty tuple
empty_tuple = ()

# 2. Create tuples for brothers and sisters
brothers = ("John", "Alex")
sisters = ("Sarah", "Emma")

# 3. Join brothers and sisters tuples into siblings
siblings = brothers + sisters
print("Siblings:", siblings)

# 4. How many siblings do you have?
num_siblings = len(siblings)
print("Number of siblings:", num_siblings)

# 5. Modify siblings tuple to add father and mother names (tuples are immutable, so we convert or join)
parents = ("David", "Mary")
family_members = siblings + parents
print("Family members:", family_members) 

# 1. Unpack siblings and parents from family_members
*siblings_unpacked, father, mother = family_members
print("Unpacked siblings:", siblings_unpacked)
print("Father:", father)
print("Mother:", mother)

# 2. Create fruits, vegetables, and animal products tuples, then join them
fruits = ("banana", "apple", "mango")
vegetables = ("tomato", "potato", "onion")
animal_products = ("milk", "meat", "cheese")

food_stuff_tp = fruits + vegetables + animal_products
print("Food stuff tuple:", food_stuff_tp)

# 3. Change food_stuff_tp tuple to food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# 4. Slice out the middle item or items
# Since length is 9 (odd number), middle index is 9 // 2 = 4
middle_index = len(food_stuff_lt) // 2
middle_item = food_stuff_lt[middle_index]
print("Middle item:", middle_item)

# 5. Slice out the first three items and the last three items
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print("First three items:", first_three)
print("Last three items:", last_three)

# 6. Delete the food_stuff_tp tuple completely
del food_stuff_tp

# 7. Check if an item exists in tuple
nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")

print("Is Estonia in nordic_countries?", "Estonia" in nordic_countries)
print("Is Iceland in nordic_countries?", "Iceland" in nordic_countries)
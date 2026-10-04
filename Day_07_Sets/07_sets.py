# Day 07

# Initial Data
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1. Find the length of the set it_companies
print(len(it_companies))

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')

# 3. Insert multiple IT companies at once
it_companies.update(['Tesla', 'Nvidia', 'Netflix'])

# 4. Remove one of the companies
it_companies.remove('Facebook')

# 1. Join A and B
A_union_B = A.union(B)

# 2. Find A intersection B
A_intersect_B = A.intersection(B)

# 3. Is A subset of B?
print(A.issubset(B))  # Returns True

# 4. Are A and B disjoint sets?
print(A.isdisjoint(B))  # Returns False

# 5. Join A with B and B with A
A_with_B = A.union(B)
B_with_A = B.union(A)

# 6. Symmetric difference between A and B
sym_diff = A.symmetric_difference(B)

# 7. Delete the sets completely
del A
del B

# 1. Convert ages to a set and compare lengths
age_set = set(age)
print("List length:", len(age))  # 8
print("Set length:", len(age_set))  # 5
# The list is bigger because sets remove duplicate values.

# 3. Unique words in a sentence
sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()
unique_words = set(words)
print("Number of unique words:", len(unique_words))
# Day 3 - Operators
# 1. Integer variable
age = 25

# 2. Float variable
height = 5.9

# 3. Complex number variable
complex_number = 1 + 2j

# 4. Area of a triangle: 0.5 * base * height
base = float(input("Enter base: "))
height_tri = float(input("Enter height: "))
area_tri = 0.5 * base * height_tri
print("Triangle Area:", area_tri)

# 5. Perimeter of a triangle: a + b + c
side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))
perimeter_tri = side_a + side_b + side_c
print("Triangle Perimeter:", perimeter_tri)

# 6. Area and perimeter of a rectangle
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area_rect = length * width
perimeter_rect = 2 * (length + width)
print("Rectangle Area:", area_rect)
print("Rectangle Perimeter:", perimeter_rect)

# 7. Area and circumference of a circle
radius = float(input("Enter radius: "))
pi = 3.14
area_circle = pi * (radius ** 2)
circumference = 2 * pi * radius
print("Circle Area:", area_circle)
print("Circle Circumference:", circumference)

# 8. Equation y = 2x - 2 (slope-intercept form y = mx + c)
slope_1 = 2
x_intercept = 1   # y = 0  ->  0 = 2x - 2  ->  x = 1
y_intercept = -2  # x = 0  ->  y = 2(0) - 2 ->  y = -2
print("Slope 1:", slope_1)

# 9. Slope between points (2, 2) and (6, 10) -> (y2 - y1) / (x2 - x1)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_2 = (y2 - y1) / (x2 - x1)

# Euclidean Distance: sqrt((x2 - x1)^2 + (y2 - y1)^2)
distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print("Slope 2:", slope_2)
print("Distance:", distance)

# 10. Compare the slopes
print("Are slopes equal?:", slope_1 == slope_2)

# 11. Find when y = x^2 + 6x + 9 equals 0 (hint: at x = -3)
x = -3
y = x**2 + 6*x + 9
print(f"When x = {x}, y = {y}")

# 12. Compare lengths (Falsy statement)
print("Falsy comparison:", len("python") != len("dragon"))

# 13. Check if 'on' is in both words
print("'on' in python and dragon?:", "on" in "python" and "on" in "dragon")

# 14. Check if 'jargon' is in the sentence
sentence = "I hope this course is not full of jargon"
print("'jargon' in sentence?:", "jargon" in sentence)

# 15. Check if 'on' is missing in both (False statement)
print("No 'on' in both?:", "on" not in "dragon" and "on" not in "python")

# 16. Convert length of 'python' to float, then to string
len_python = len("python")
float_len = float(len_python)
str_len = str(float_len)
print("String length:", str_len)

# 17. Check if a number is even (remainder is 0 when divided by 2)
num = 4
print("Is even?:", num % 2 == 0)

# 18. Floor division vs int conversion
print("7 // 3 == int(2.7)?:", 7 // 3 == int(2.7))

# 19. Type check: string vs integer
print("type('10') == type(10)?:", type("10") == type(10))

# 20. Int conversion of decimal string '9.8'
# '9.8' must be float first before int, otherwise it causes an error
print("int(float('9.8')) == 10?:", int(float("9.8")) == 10)

# 21. Weekly pay calculator
hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
print("Your weekly earning is:", hours * rate)

# 22. Seconds lived calculator
years = int(input("Enter number of years lived: "))
seconds = years * 365 * 24 * 60 * 60
print(f"You have lived for {seconds} seconds.")

# 23. Print the number table
# Row format: number  1  number  number^2  number^3
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)

    
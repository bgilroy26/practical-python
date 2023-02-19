# bounce.py
#
# Exercise 1.5
starting_height = 100
height = starting_height
bounce_proportion = 0.6
bounce_count = 0

while height > 0.00005:
    print(bounce_count, height)
    height = height * bounce_proportion
    bounce_count = bounce_count + 1

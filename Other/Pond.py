point = input()

mokhtasat = point.split(" ")
x = float(mokhtasat[0])
y = float(mokhtasat[1])

# 0 for outside, 1 for inside, 2 for on lines
Location = 1


# checking Lower sides of the pentagon
if -5 <= x and x <= -1.5:
    if y < (-1.5/3.5 * x - 30.25/3.5):
        Location = 0
    elif y == (-1.5/3.5 * x - 30.25/3.5):
        Location = 2

elif -1.5 < x and x <= 4.5:
    if y < (9.5/6 * x - 33.75/6):
        Location = 0
    elif y == (9.5/6 * x - 33.75/6):    
        Location = 2
else:
    Location = 0

# checking Upper sides of the pentagon
if -5 <= x and x <= -2.75:
    if y > (11/2.25 * x + 40.375/2.25):
        Location = 0
    elif y == (11/2.25 * x + 40.375/2.25):
        Location = 2

elif -2.75 <= x and x <= 2.75:
    if y > (2/5.5 * x + 30.25/5.5):
        Location = 0
    elif y == (2/5.5 * x + 30.25/5.5):
        Location = 2

elif 2.75 <= x and x <= 4.5:
    if y > (-5/1.75 * x + 25.125/1.75):
        Location = 0
    elif y == (-5/1.75 * x + 25.125/1.75):
        Location = 2


if (Location == 1):
    print("Fall into the pond")
else:
    print("Not fall into the pond")

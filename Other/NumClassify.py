limit = int(input())
print("Checking numbers from 2 to %d :" % limit)

Odds = [0, 0]
Odds_counter = 0
Evens = [0, 0]
Evens_counter = 0
Squares = []
Squares_counter = 0
Cubes = []
Cubes_counter = 0

for i in range(2, limit+1):

    if i % 2 == 1:
        if Odds[0] != 0:
            Odds[1] = i
        else:
            Odds[1] = i
            Odds[0] = i
        Odds_counter += 1

    else:
        if Evens[0] != 0:
            Evens[1] = i
        else:
            Evens[1] = i
            Evens[0] = i
        Evens_counter += 1

    if i**2 <= limit:
        Squares.append(i**2)
        Squares_counter += 1

    if i**3 <= limit:
        Cubes.append(i**3)
        Cubes_counter += 1

if Odds[0] != 0:
    print("Odd (%d) : %d...%d" % (Odds_counter, Odds[0], Odds[1]))
else :
    print("Odd (%d) : " % Odds_counter)

if Evens[0] != 0:
    print("Even (%d) : %d...%d" % (Evens_counter, Evens[0], Evens[1]))
else:
    print("Even (%d) : " % Odds_counter)

print("Square :", Squares)
print("Cube :", Cubes)
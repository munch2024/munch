# This code generates Pythagorean triples (a, b, c) where 'c' is the hypotenuse,
# with all sides ranging from 1 to 20.

for c in range(1, 21):
    for b in range(1, c):
        for a in range(1, b):
            if a**2 + b**2 == c**2:
                print(f'{a} {b} {c}')

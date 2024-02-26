# This code generates Pythagorean triples (a, b, c) where 'c' is the hypotenuse,
# with all sides ranging from 1 to 20.

# Loop over possible values for the hypotenuse 'c' from 1 to 20.
for c in range(1, 21):
    # Loop over possible values for side 'b' from 1 to 'c' exclusive.
    for b in range(1, c):
        # Loop over possible values for side 'a' from 1 to 'b' exclusive.
        for a in range(1, b):
            # Check if the current values of 'a', 'b', and 'c' form a Pythagorean triple.
            if a**2 + b**2 == c**2:
                # If the condition is met, print the Pythagorean triple.
                print(f'{a} {b} {c}')

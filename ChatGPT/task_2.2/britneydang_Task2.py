import main
def solve_quadratic_equation(a, b, c):
    # Calculate the discriminant
    discriminant = (b ** 2) - (4 * a * c)

    # Calculate solutions
    sqrt_discriminant = cmath.sqrt(discriminant)
    ans1 = (-b - sqrt_discriminant) / (2 * a)
    ans2 = (-b + sqrt_discriminant) / (2 * a)

    return ans1, ans2

# Print instructions for the user
print("Quadratic equations are in the form of ax^2 + bx + c = 0.")
print("Do not use 0 as the value of a")
print(" ")

# Input values for a, b, and c
a = float(input("Enter a value for a (not 0): "))
b = float(input("Enter a value for b: "))
c = float(input("Enter a value for c: "))
print(" ")

# Solve the quadratic equation
solution1, solution2 = solve_quadratic_equation(a, b, c)

# Print solutions
if solution1 == solution2:
    # If both solutions are equal, print only one solution
    print("The solution is:", solution1)
else:
    # If solutions are different, print both solutions
    print("The first solution is:", solution1)
    print("The second solution is:", solution2)
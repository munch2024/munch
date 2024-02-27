import cmath

print("Quadratic equations are in the form of ax^2 + bx + c = 0.")
print("Do not use 0 as the value of a")

print(" ")

a = input("Enter a value for a (not 0): ")
b = input("Enter a value for b: ")
c = input("Enter a value for c: ")

print(" ")

if int(b) == 0:
  x = -(4 * int(a) * int(c))
else:
  x = (int(b)**2) - (4 * int(a) * int(c))

ans1 = (-int(b) - cmath.sqrt(x)) / (2 * int(a))
ans2 = (-int(b) + cmath.sqrt(x)) / (2 * int(a))

print(" ")

if ans1 == ans2:
  print("The solution is:-")
  print(ans1)
else:
  print("The first solution is:-")
  print(ans1)
  print("The second solution is:-")
  print(ans2)

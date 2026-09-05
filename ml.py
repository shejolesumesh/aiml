a,b = map(int, input("Enter two numbers separated by a comma: ").split(','))

print("Before swapping: a =", a, "b =", b)
a,b = b,a
print("After swapping: a =", a, "b =", b)
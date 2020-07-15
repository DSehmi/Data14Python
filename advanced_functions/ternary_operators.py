# Ternary Operators
# Conditional Expressions
# 3 Parts to them

age = 17

# Method1
if age >= 18:
    print("Go ahead!")
else:
    print("Go away!")

# Method2
print("Go ahead!" if age >= 18 else "Go away!")

# Method3
print(("Go away!", "Go ahead!")[age >= 18])  # don't use this method

# Method4
status = "Go ahead!" if age >= 18 else "Go away!"
print(status)

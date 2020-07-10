# WHILE LOOPS
# These will continue forever until the thing becomes true

counter = 0

while counter < 10:
    print(f"Still counting! {counter}")
    if counter == 6:
        break
    counter += 1

print("We've escaped the while loop")

x = "13a"
print(x.isnumeric())

age_input = ""

while not age_input.isnumeric():
    age_input = input("Enter your age\n")
    if not age_input.isnumeric():
        print("That is not a number, try again")

age = int(age_input)

print("You are " + str(age))

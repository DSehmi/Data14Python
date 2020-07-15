# Lambda
# a way of doing anonymous functions
# doing functions without having to define the function in advance


def add(n1, n2):
    return n1 + n2


print(add(2, 2))

add_lambda = lambda n1, n2: n1 + n2
print(add_lambda(2, 2))

# We can use lambdas with maps
# so that we don't have to define the function before mapping

numbers = [181, 2834, 2, 283, 3]

results = map(lambda x: x*x+3, numbers)
print(list(results))

# In a new list called bonus,
# savings with 10% added

savings = [234.00, 555.00, 674.00, 78.00]

bonus = list(map(lambda x: x * 1.1, savings))
print(bonus)

# In a new list called even_savings
# keep only savings amounts that are even

even_savings = list(filter(lambda x: x % 2 == 0, savings))
print(even_savings)

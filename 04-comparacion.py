import random

n1 = 10
n2 = 15

# New variables with random numbers
n3 = random.randint(1, 100)
n4 = random.randint(1, 100)
n5 = random.randint(1, 100)

print(n1 == n2)  # False
print(n1 > n3)   # True or False depending on the value of n3
print(n2 < n4)   # True or False depending on the value of n4
print(n3 != n5)  # True

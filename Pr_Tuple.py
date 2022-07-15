tup = (9,8,62,692,98,399,52,36,98)
print("Type of tup is:", type(tup))

# built in functions of tuple are:
# 1. len:
print('Length of tuple is:', len(tup))

# 2. max:
print('Maximum value in tuple is:', max(tup))

# 3. min:
print('Minimum value in tuple is:', min(tup))

# 4. count:
c=tup.count(98)
print(c,"times occurs 98 in tuple.")

# 5. index:
i= tup.index(98)
print("Index of 98 is:", i)

# 6. sorted:
sorted(tup)
print("Sorted tuple is:",tup)

# 7. sum:
print("The sum of elements present in given tuple is:",sum(tup))

Numbers = []
for a in range(1, 21):
    Numbers.append(a)
print("The given list is:", Numbers)

print("The Prime numbers in list are: ", end=" ")

for num in range(1, 21):
    if num > 1:
        for j in range(2, num):
            if (num % j == 0):
                break
        else:
            print(num, end=" ")

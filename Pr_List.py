# Declare a  List;

l = [98,56,77,6,85,1,85,75,11,82,88,11]

#Four built-in functions of list are follow as :
# 1. len:
print("Length of list is: ", len(l))

# 2. min:
print("The minimum value in list is:", min(l))

# 3. max:
print('The maximum value in list is:', max(l))

# 4. sum:
print("The sum of list is:", sum(l))

# 5. count:
c = l.count(11)
print (c,"Times 11 occurs in list.")

# 6. reverse:
l.reverse()
print("List in reverse format is : ",l)

# 7. sort:
l.sort()
print("Sorted list is: ", l)

# 8. append:
l.append(101)
print("The updated list is after 101 append is: ", l)

# 9. pop:
print("The deleted element from 7 index is: ", l.pop(7))

users = ["Papa", "Mommy", "Edward", "Martin"]
non_users = ["Bob", "Jon"]
print(users[0:])
print(len(users))
print(users[0:4])
print(users[-1])
print(users[-2:-1])

users.append('Mamou')
print(users)

users += ["Ninie"]
print(users)

users.extend(["Mima", "Pipa"])
print(users)
# users.extend(non_users)
# print(users)

users.insert(0, 'Erika')
print(users)
users[2:2] = ['Roman', 'Adrien']
print(users)

users[4:5] = ['Papou', 'Sylvie']
print(users)

users.remove('Adrien')
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

# del non_users
# print(non_users)

non_users.clear()
print(non_users)

users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [7, 9,5, 16, 11, 20, 13, 27, 36]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

# Does not modify the original list
print(sorted(nums, reverse=True))
print(nums)

nums_copy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(nums)
print(nums_copy)
print(mynums)
print(mycopy)

print(type(nums))

# Tuples CANNOT BE CHANGED§
mytuple = tuple(('Phil', 40, True))

another_tuple = (18, 27, 36, 99)
print(mytuple)
print(type(another_tuple))

new_list = list(mytuple)
new_list.append('Carole')
newtuple = tuple(new_list)
print(newtuple)
print(mytuple)

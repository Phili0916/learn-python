value = 1
# Will itereate up to 9
# while value < 10:
#     print(value)
#     value += 1

# Will itereate up to 10
# while value <= 10:
#     print(value)
#     value += 1

# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1

names = ["Jon", "T-Bone", "Casey"]

# for name in names:
#     print(name)

# for x in "Mississippi":
#     print(x)

# The loop will stop before it iterates to Casey
# for name in names:
#     if name == "Casey":
#         break
#     print(name)

# The loop will iterate over T-Bone
for name in names:
    if name == "T-Bone":
        continue
    print(name)

# Will print the range of numbers starting from 0 and up to 4 but not including 4
for x in range(4):
    print("x = " + str(x))

# Will print from the number to start from but not include the number you stop on
for n in range(2, 9):
    print("n = " + str(n))

# you can add how much to increment by with the 3rd parameter
for y in range(1, 100, 5):
    print("y = " + str(y))
else:
    print("Glad that\'s over")

# Let's create a nested loop
dudes = ["DJ", "Nick", "Rico"]
actions = ["smokes", "drinks", "raids"]

for dude in dudes:
    for action in actions:
        print(dude + " " + action + "!")
# Dictionaries are used to store data that are in key/value pairs...like objects in javascript

band = {
    "vocals": "Paul",
    "guitar": "George"
}

band2 = dict(vocals="Mick", guitar="Keith")

print(band)
print(band2)

print(type(band))
print(len(band2))

# Access Items by passing the Key

print(band["vocals"])
print(band2.get("guitar"))

# List all Keys
print(band.keys())

# List all Values
print(band2.values())

# List of Key/Value Pairs as tuples
print(band.items())

# Verify if a key exists in a dictionary
print("guitar" in band)
print("cowbell" in band2)

# Change Values
band["vocals"] = "John"
print(band)
band.update({"drums": "Ringo"})
print(band)

# Remove Items
band.pop("drums")
print(band)

band["drums"] = "Ringo"
print(band.popitem()) #tuple
print(band)

# Delete and Clear
band["drums"] = "Ringo"
del band["drums"]
print(band)

band2.clear()
print(band2)
del band2

# Copy Dictionaries
# band2 = band # creates a reference and not an actual copy

band2 = band.copy()
band2["guitar"] = "Erik"
print(band)
print(band2)

# Use the dict constructor function
band3 = dict(band)
print('Good Copy')
print(band3)

# Nested Dictionarie This means the value for a dictionary can be another dictionary

member1 = {
    "name": "Fat Mike",
    "instrument": "bass"
}

member2 = {
    "name": "Smelly",
    "instrument": "drums"
}

band4 = {
    "member1": member1,
    "member2": member2

}

print(band4)
print(band4["member1"]["name"])
print(band4["member1"]["instrument"])

# Sets

nums = {1, 2, 3, 4}
nums2 = set((5, 6, 7, 8))

print(nums)
print(nums2)
print(type(nums))
print(len(nums2))

# No duplicates are allowed in a set
nums3 = {9, 9, 10, 11, 12}
print(nums3)

# True is a duplicate of 1 and False is a duplicate of 0
nums4 = {1, 2, True, False, 3, 4, 0}
print(nums4)

# check if a value is in a set
print(2 in nums)

# add a new value to a set
nums.add(8)
print(nums)

# add elements from one set to another
nums.update(nums2)
print(nums)

# You can use update with lists, tuples, and dictionaries

# Merge two sets to create a new set
one = {1, 2, 3, 4}
two = {5, 6, 7, 8}
three = one.union(two)
print(three)

# keep only the duplicates in each set
four = {1, 2, 3}
five = {2, 3, 4}
four.intersection_update(five)
print(four)

# keep everything except the duplicates
four = {1, 2, 3}
five = {2, 3, 4}

four.symmetric_difference_update(five)
print(four)

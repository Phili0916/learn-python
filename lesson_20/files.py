
# Read
# Append
# Write
# Create

import os


##### Read - error if file doesn't exist #####

for f in os.listdir("/Users/Philip/python-projects/learn-python/lesson_20/"):
    print(f)

f = open("lesson_20/names.txt", "r")
print(f.read())

# print(f.readline())

f.close()

try:
    f = open("does_not_exist", "r")
    print(f.read())
except:
    print("File you want to read doesn't exist")
finally:
    f.close()

##### Append - creates a file that doesn't exist #####

f = open("lesson_20/names.txt", "a")
f.write(f"\nSam")
f.close()

f = open("lesson_20/names.txt", "r")
print(f.read())
f.close()


###### Write - You can overwrite in your file #####

f = open("lesson_20/context.txt", "w")
f.write("I can add text to my file")
f.close()

f = open("lesson_20/names.txt", "r")
print(f.read())
f.close()

##### Two ways to create a new file #####

# Opens a file for writing #

f = open("lesson_20/new_names_list.txt", "w")
f.close()

# creates new file but will return an error if the file already exists
if not os.path.exists("lesson_20/more_names.txt"):
    f = open("lesson_20/more_names.txt", "x")
    f.close()

##### Delete a File #####

if os.path.exists("lesson_20/new_names_list.txt"):
    os.remove("lesson_20/new_names_list.txt")
else:
    print("The file you wish to delete does not exist")
name = "Phil"

def greeting(firstname):
    color = "blue"
    print(color)
    print(name)
    print(firstname)

greeting("Jon")

def another_function():
    greeting("Nick")

another_function()

count = 1
# You cannot redefine a global variable inside a local scope. You need to add the global keyword in front
def count_numbers():
    global count
    count += 1
    print(count)

count_numbers()

# You can reasign local variables with the nonlocal keyword

def baseball_function():
    favorite_team = "Mets"
    print(favorite_team)

    def team_function():
        nonlocal favorite_team
        favorite_team = "Rangers"
        print(favorite_team)

    team_function()

baseball_function()
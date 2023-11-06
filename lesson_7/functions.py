def hello():
    print("Hello World")

hello()

def sum(num1, num2):
   if(type(num1) is not int or type(num2) is not int):
       return
   return num1 + num2

total = sum("a", 9)
print(total)

def multiple_items(*args):
    print(type(args))
    print(args)
 
multiple_items("Jon", "Casey")

def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

mult_named_items(first = "Jon", last = "Casey")
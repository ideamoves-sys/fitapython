#creating a clean repetable code is a key part of becoming an effective programmer.
#Functions allow us to create blocks of code that can be easily executed manyu times without needing to constantly rewrite the entire
#block of code
#Need to combine and work the the if forr loops with function to write a better program

#CREATING A FUNCTION:
#creating a function requires a very specific syntax, including the def keyword, correct indentation and proper structire

#def is a keyword (definition)
#def is the keyword telling python this is a function followed by function name snake casing
#def my_func(arg/params):

#example for function

def greet():
    "doc string if any"
    print("hello")
#to call the function we need to use greet
greet() #it will print the output as hello

#little complex function
def greet_one(name):
    "accept args to be passed by the user"
    print("Hello" + name)
greet_one("Kumar")

#function with return
def add_function(num1, num2):
    return num+num2
result = add_function(1,2)
print(result)

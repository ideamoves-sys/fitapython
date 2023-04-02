
def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'Even'
    else:
        return mystring[0]

# Define a function to convert a string to uppercase
def to_uppercase(s):
    return s.upper()

# Define a list of strings
words = ['apple', 'banana', 'cherry', 'date', 'elderberry']

# Use the map function to apply the to_uppercase function to each element in the list
uppercase_words = map(to_uppercase, words)

# Convert the map object to a list to see the results
print(list(uppercase_words))

# Define a function to convert a string to uppercase
def to_uppercase(s):
    return s.upper()

# Define a list of strings
words = ['apple', 'banana', 'cherry', 'date', 'elderberry']

# Use a for loop to apply the to_uppercase function to each element in the list
uppercase_words = []
for word in words:
    uppercase_words.append(to_uppercase(word))

# Print the results
print(uppercase_words)


#filter
def check_even(num):
    return num%2 == 0

mynums = [1,2,3,4,5,6]

for n in filter(check_even, mynums)

#normal functo to lambda
def sqr(num):
    res = num ** 2
    return res
#lambda function with no keyword def and method name
sqr = lambda num: num ** 2

#combine map and lambda and filter
# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use map function with lambda to square each number in the list
squared_numbers = map(lambda x: x**2, numbers)

# Use filter function with lambda to filter out odd numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers)

# Print the results
print(list(squared_numbers))
print(list(even_numbers))

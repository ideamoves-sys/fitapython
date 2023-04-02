#PRINTFORMATTING WITH STRINGS

#-----------------------------------------------------------------------------------------------#
#USUAL WAY OF CONCATING String

my_name ="Kumar",
print("Hello", my_name)

#Actucally there are multiple ways to format strings for printig the variables in them
#This is known as "STRING INTERPOLATION"

#2 methods are there for This
    1) .format() method
    2) f-strings(formatted string literals)

#.format method

print('this is a string {}'.format('INSERTED'))
#here wat r we doing is, like the {} is where the text get filled from the .format

#insert many things
print('The {} {} {}')
#it will be come in the same order no changes in order

#yu can fill up the {} with index like {2} {1} {0}

#Can give the key words as well
#print('The {q} {b} {f}'.format(f='fox', b='brown',q='quick')) preferrable

#format string literlas ,method
name = "abc"
print('hello, his name is {}'.format(name))

#can be replace like below
print(f'hello his name is {name})

#multiple variables
namee = "kumar",
age = 28
print(f'{name} is {age} years old')
#-----------------------------------------------------------------------------------------------#

=====================================================================================================

# //These are the basic building blocks when constructing the larger pieces of code.
# do some baic mathemetic operations
# +,-,%,/
# explain basic + and *
# quiz ====> floating number 36 mul , 1/2 in python3
# print(6*6)

=====================================================================================================

=====================================================================================================

# //VARIABLE ASSIGNMNETS
# RULES FOR VAR NAMES
# NAMES SHOULDNT START WITH number
# THERE CAN BE NO SPCAES INSTEAD CAN USE __
# CANT USE ANY SYMBOLS
# USE LOWERCAE FOR VARIABLES
# SHODULN'Y RESERVED KEY WORDS LIKE STR AND LIST

# my_dogs = 2
# my_dogss = ["sam", "ash"] it's is okat it is dynamically tyoes pros and cons explain

=====================================================================================================

=====================================================================================================

# //Numerics
a = 5;
print(a)

# a = a + a is possbible ask qs

type(a)

my_income = 100;
tax_rate = 0.1;
my_taxes = my_income * tax_rate;
print(my_taxes)


# Strings using '' or ""
# " I don't want to ln " use double quotes in this case
# STRINGS ARE ORDERED SEQUENCES MEANING WE CAN USE INDEXING AND SLICING TO GRAB SUB-SECTIONS OF THE STRING
# REVERESE INDEXING O -4, -3, -2, - REGARDLESS LENGTH OF STRING
MY_STR = 'HELLO'
MY_QT = 'i'm GOING ON A RUN BUT YOU USE DOUBLE QUOTES
# HELLO WORLD, HELLO World 2

# BACKSLAH (\N) ESCAPE CHAR \T FOR TAB
PRINT('HELLO \N WORLD')
LEN OF STR len('I AM')

# Your Task:
# Use what you know about the print() function to print out the phrase "Hello World" .
# Make sure your capitalization and spacing match.
=====================================================================================================

=====================================================================================================

# STRING INDEXING
mystr = "Hellow World"
print(mystr[0])
# ask for R

# reerse indexing
print(mystr[-2])

# SLICING[START:STOP:STEP]
# START: IS A NUMERICAL INDEX FR THE SLICE START
# STOP: IS THE INDEX YOU WILL GO UP TO BUT NOT INCLUDE
# STEP: IS THE SIZE OF THE JUMP YOU TAKE

mystr = 'abcdefghijk'
print(mystr);
print(mystr[2])//only ChildProcessError
print (mystr[2:]) //all the way to end
print (mystr[:3]) //till d //stop idex will not include index position
print (mystr[3:6]) //btwn d and f ===> def
print(mystr[::]) //select all the item
print (mystr[::2]) // stepsize will jum 2 chars and print
print (mystr[::-1]) //  reverse

# Home work
# String Indexing
# Write a string index that returns just the letter 'r'  from 'Hello World' .
# For example, 'Hello World'[0]  returns 'H'
# You should only write one line of code for this. Do not assign a variable name to the string.
=====================================================================================================

#
# String Slicing
# Use string slicing to grab the word 'ink'  from inside 'tinker'
#
# For example, 'education'[3:6]  returns 'cat'
#
# Remember that when slicing you only go up to but not including the end index.
#
# You should only write one line of code for this. Do not assign a variable name to the string.


# //STRING PROPERTIES AND METHODS
# //string is immutable
# name = "Sam"; name[0] = "A"

name ="Sam"
ll = name[1:]
print(ll)

# //concatenate
'P' + ll

# //MULTIPLY
LETTER = 'Z';

print(letter *10)

# SHOULD NOT CONCATENATE BUMBER AND STRING
'2' + '3'

# //BUILT IN STRING METHODS
X = 'HELLO WORLD';
X.upper();
X.Split(); -,+ or ws
# it will effect the original string

# TASK:
# Strings are immutable.
# If s='hello' what is the output of s[1]
# If s='Sammy' what is the output of s[2:]?

=====================================================================================================

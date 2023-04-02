#to control the flow logiv we use some keywords: 1)if 2)elif 3)else

#In control flow syntax make use of colons and indentation(white space)
#this indenattaion system is important in python instead if {} like in another pgm we won't use in python instead we use indentation

#syntax of if statement
#if some_condition:
    #excecute some code
#else:
    #excecute something else code

#if some_condition:
    #excecute some code
#elif some_condition:
    #excecute something else code
#else
    #excute else code

#if code example

#if True:
    #print('It is true')

hungry = True;
if hungry:
    print('feed me')

#if else
if hungry:
    print('feed me')
else:
    print('I am done')

#if elif else

location = 'Bank'

if location == 'Garage':
    print('Alter the car')
elif location == 'Bank':
    print('Withdraw money')
else:
    print('Sorry not a valid selection')

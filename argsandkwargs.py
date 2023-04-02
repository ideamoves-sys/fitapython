#*args and **kwargs it is functional parameter (arguments and keyword arguments)

#creating a function(accept 2 numbers)
def myfunc(a,b):
    #Returns 5% of the sum of a and # b here an and b are positional arguments try to give extra param you'll get error
    return sum((a,b)) * 0.05

myfunc(40,60)

def myfunctwo(*args): #this *args will treat the incoming args as tuple so I can give any number of arguments
#instead of args we can give any name args is convention
#it returns tuple
print(args) #it will show you it's structure
    return sum(args) * 0.05

myfunctwo(40,60,70,80)

#*args and for loops
def myfuncthree(*args):
    for item in args:
        print(item)

#**kwargs that build dict of key value pairs it returns dict instead of kwargs you can use any name
def myfuncfur(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('my friut of choice is {}'.format(kwargs['fruit']));
    else:
        print('no fruit')
myfuncfur(fruit='apple', veggie='spinach')

#combination of args and kwargs
def myfuncfive(*args, **kwargs): #order matter's here(argsfirst, and kwargs) whnen giving args
    print('I would like {} {}'.format(args[0], kwargs['food']))
myfuncfive(10,20,30fruit="orrange", food="eggs", animals="dog")

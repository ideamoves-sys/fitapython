#scope

x = 25


def printer():
    x = 50
    return x

print(x)#what is the OP

print(printer())


name  = 'This is a global string'

def greet():
    name = 'Sammy'

    def hello():
        print('hello' + name)

    hello()

greet()

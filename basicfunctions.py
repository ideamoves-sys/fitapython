def say_hello():
    print("hello")
    print("how")
    print("are")
    print("you")
say_hello() #should call function with ()


def greet(name): #default value  name='kumar'
    print(f'hello {name}')
greet('Kumar') #if you miss passing the argument python will give error

#Return keyword

def add_num(num1,num2):
    return num1+num2

res = add_num(10+30)

#FUNCTIONS with LOGICS
def even_check(num):
    result = num % 2 == 0
    return result
#
# def even_check(num):
#     return num % 2 == 0

even_check(10)


#Function with mylist

#return true if any number is even in the list
def check_even_list(num_list):
    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            pass #don't do anything
    return False
check_even_list([3,5,7]) #don't return anything
check_even_list([2,4,6])
check_even_list([2,4,6,3,5])

#Return all the even number in a num_list
def even_list(num_list):
    even_num = []

    for number in num_list:
        if number % 2 == 0:
            even_num.append(number)
        else:
            pass
    retrun even_num

even_list([2,4,6])
even_list([1,3,5])

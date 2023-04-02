#the term iterbale means you can iterate over the object
#for example we can iterrate over every character in string, iterate over every item in a list, iterate over every key in dict

my_list = [1,2,3,4,5,6,7,8,9,10]

# for num in my_list:
#     print num
# #example 2
# for num in my_list:
#     print('hello') #it will print hello 10 times

#combining if and for loop
for num in my_list:
    if num % 2 == 0:
        print( f"even number:{num}")
    else :
        print(f"odd number:{num}")

#example 2
list_sum = 0

for num in my_list:
    list_sum = list_sum + sum
print(list_sum) #print inside and show the op

#example3
my_String = 'Hello World'
for letter in my_String:
    print(letter)

#tuple
tup = (1,2,3)
for item in tup:
    print(item)

#list with tuple
my_lst = [(1,2),(3,4),(5,6),(7,8)]
for item in my_lst:
    print(item)

#tuple unpacking
for (a,b) in my_lst: #don't need () for a, b
    print(a)
    print(b)

#iterate dict
d = {'k1':1, 'k2':2, 'k3':3}
for item in d:
    print(item)

#to iterate the items
for item in d.items():
    print(item)

#tuple unpacking in dict
for key, value in d.items():
    print(value)

#value
for value in d.values():
    print(value)

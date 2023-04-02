# It is a unique way of creating a list with python
#if you find using a for loop alog wth .append to create a list, List

#example
my_str = 'hello'
mylst = []

for letter in my_str :
    mylst.append(letter)

print(mylst)

#single line #llist comprehension

mylist = [letter for  letter in my_str]
print(mylist)

mynum = [num for num in range(0,11)]
print(mynum)

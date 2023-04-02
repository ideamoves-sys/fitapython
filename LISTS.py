#lists are ordered sequences that can hold a variety of obj types
#They use [] bracekts and commas to seprate objects in the list.
#Lists supports indexing and slicing. Lists can be nested and also have a variety of useful methods that can be called off them.
#WE CAN MUTATE THE LIST UNLESS STRING

#Indexing
my_List = ['one', 'two', 'three']
len(my_List)
my_list[0]

#Slicing
my_mixed_list = ['two', 3, 4.5]
my_mixed_list[1:]

#Concatenation
my_anotherlist = ['four', 'five']
res = my_List + my_anotherlist
print(res)

#MUTATE Lists
res[0] = 'ONE ALL CAPS'
print(res)

#ADD AN ELEMENT AT THE END OF THE Lists
res.append('six'); #place the item at the end of the item
print(res)

#pop out the item from end of the item
res.pop() #it will give the op of removed item
print(res)

#remove the sepcific index
res.pop(0) #give the index reverse index will also work
print(res)

#Sort
new_lIST = ['a','e','x','b','c']
new_lIST.sort()
prtint(new_lIST)

#EXPLAIN NONE LIKE NULL

num_list [4,1,8,3]
num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)

#quizz
#If lst=['a','b','c'] What is the result of lst[1:]?
#If lst=[0,1,2] what is the result of lst.pop()?
#Lists can have multiple object types?

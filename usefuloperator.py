#useful operators and builtin functions

#RANGE

mylist = [1,2,3]

for num in range(10): #will generate num till 9
    print(num)

for num in range(3, 10):
    print(num)

#step
for num in range(0, 10, 2):
    print(num)

#if you give range alon with list it's a generator
list(range(0,11,2))


#ENUMURATE
index_count = 0

#generic example
for letter in 'abcde':
    print('AT index {} the letter is {}'.format(index_count, letter))
    index_count += 1

#enumurate example
word = 'abcde'

for item in enumerate(word): #enumrate will be taken care of the inde automatically
    print(index)

#ZIP
mylist = [1,2,3]
mylist1 = ['a','b','c']

for item in zip(mylist, mylist2):
    print(item)

#IN operator
'x' in [1,2,3]
'x' in ['x','y','z']


mystrlist = [10,20,30,40,100]
min(mystrlist)
max(mystrlist

#RANDOM(import llirbary)
from random import  shuffle
myl = [1,2,3,4,5,67,8,9,10]
shuffle(myl) // this can't be put in varilable

from random import randint
randint(0,100)


#accept user input
res = input('what is your name: ')
#int(input('enter a num'))

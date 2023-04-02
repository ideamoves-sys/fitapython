#It's very similar to lists , it's not mutable is the only difference.
#Once an element is inside a tuple it can not be reassigned
#(1,2,3)

tup = (1,2,3) #type(tup)
len(tup)
my_list = [1,2,3] #list

#mixed datatype inside tuple
t = ('one', 2)
print(t)

#can do slicing and indixing
tup[1] # can do reverese(-1) also

#countand index tuple methods
my_tup = ('a','a',2)
my_tup.count('a') #returns the a count
my_tup.index('a') #returns the very first index where a is occuring

#immutablity of tuple it will throw error type error
#when app becomes larger

#questions

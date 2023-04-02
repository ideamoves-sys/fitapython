#sets are unordered collections of unique elements

myset = set()
print(myset)

#adding obj to sets
myset.add(1) #it looks like dict but no because there is no key:value pair
myset.add(2)
myset.add(2) #it will not repeate the number it will have a unoque value
my_list = [1,1,1,1,1,2,2,2,2,3,3,3]
res = set(my_list)
print(res)

#QUESTION: What is the result of:set([1,1,2,3])

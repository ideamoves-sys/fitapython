#dictionaries use curly braces and colons o signy the keys and their associated values
#{'key1':'value1','key2':'value2'}
#so when to choose list and when to choose a dict?
#DICT: Objects reterived by key name (unordered and cannot be sorted)
#LISTS: Objects reterived by location (ordered sequence can be indexed or sliced)

my_dict = {'key1':'value1', 'key2':'value2'}
print(my_dict)

#get the specific key
a = my_dict['key1']
print(a)

#example
prices = {'apple':2.99, 'oranges':1.99,'milk':5.88}
b = prices['apple']

#dict with multiple values
d = {'k1':123, 'k2':[0,1,2], 'k3':{'insidekey':100}}
c = d['k2'] #d['k2'][1] what will be the op
e = d['k3'] #will return k3 completely
f = d['k3']['insidekey']
print(C)
print(e)#will return k3 completely
print(f)#will return k3 insidekey only


#example 2
{'key1':['a','b','c']}
my_list = d['key1']
print(my_list)

lettr = my_list[2] #will give value from index
letter.upper()

secondway = d['key1'][2].upper() #one liner
print(secondway)


#add new key value pair to dictionaries
new_d = {'k1':100, 'k2':200}
re = new_d['k3'] = 300
print(re)

#override exsisting key word
new_res = new_d['k1'] = 'new value'
print(new_res)

#dict METHODS
dict_method = {'k1':100, 'k2':200}

dict_method.keys()
dict_method.values()
dict_method.items() #it will return complete dict

#questions

#Given d={'k1':[1,2,3]} What is the output of d['k1'][1]
#

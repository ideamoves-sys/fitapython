#reading files r to read file W- to write in file a- to append in file
#r+ is for reading and writing
#w+ writing and reading

myfile = open('test.txt', "r")
content = myfile.read();
print(content)
#to reset the cursor you need to use seek(0)

#readlines
mf = open('test.txt', "r")
con = mf.readlines()
print(con)


#if the file is in diff folder theen in windows we need to pass wholefile path with double backslash \\
#if your are in mac use forward slash

#to close
mf.close()


#new way of opening file in this way we no need to worry about closing the file

with open('test.txt') as new_file:
    contennt = new_file.read()
print(contennt)


#writing in the files

# with open('test.txt', mode='w') as myfile:
#     conn = myfile.read()

#examples
with open('mynewfile.txt', mode='r') as f:
    print(f.read())

with open('mynewfile.txt', mode='a') as f:
    f.write('FOUR ON FOUR')
print(f)

with open('mynewfileone.txt', mode='w') as f:
    f.write('I created this fileR')
print(f) #it wil override if the file is already available

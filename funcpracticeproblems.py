#lesser of Two evens: write a function that returns the lesser of 2 given numbers if both num are even,
# but return the greater if one or both numbers are odd
#lesser_of_two_evens(2,4) ----> 2
#lesser_of_two_evens(2,5) ----> 5

def lesser_of_two_evens(a,b): # 1st method
    if a%2 == 0 and b%2 == 0:
        #Both the numbers are even_num
        if a < b :
            result = a
        else:
            result = b
    else:
        #one or both numbers are odd
        if a > b:
            result = a
        else:
            result = b;
    return result

lesser_of_two_evens(2,5)
#method # B if you want to mass more than two values in min and max you have to send as list
def lesser_of_two_evens(a,b): # 1st method
    if a%2 == 0 and b%2 == 0:
        #Both the numbers are even_num
        result = min(a,b)
    else:
        #one or both numbers are odd
        result = max(a,b)
    return result

#method 3
def lesser_of_two_evens(a,b): # 3rd method if you use return the program has to wwait till it checks the condition
    if a%2 == 0 and b%2 == 0:
        #Both the numbers are even_num
        return min(a,b)
    else:
        #one or both numbers are odd
        return  max(a,b)

#Animal crackers: write a function takes a two-word string and returns tru if both words beign with same letter
#animal_crackers('Levelheaded Llama') --> True
#animal_crackers('crazy kangaroo) --> False
def animal_crackers(text):
    wordslist = text.split()
    print(wordslist) #print it and show animal_crackers('Levelheaded Llama')
    first = wordslist[0]
    second = wordslist[1]

    return first[0] == second[0]

def animal_crackers(text): #mwthod 2
    wordslist = text.lower().split() # you can do this split with anothe rvar also
    print(wordslist) #print it and show animal_crackers('Levelheaded Llama')
    return wordslist[0][0] == wordslist[1][0]

#makes Twenty: Givem two int, return true if the sum of the int is 20 or if one of the int is 20. If not , return is False
#make_twenty(20,10) ==> True
#makes_twenty(12,8) ==> true
#makes_twenty(2,3)  ==> false

def make_twenty(n1,n2):
    if n1 + n2 == 20:
        return True
    elif n1 == 20;
        return True
    else:
        return False

#mwthod2

def make_twenty(n1,n2):
    return (n1+n2) == 20 or n1 == 20 or n2 ==20
    if n1 + n2 == 20:
        return True
    elif n1 == 20;
        return True
    else:
        return False

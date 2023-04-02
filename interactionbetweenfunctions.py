#find red balls game using python
#things we'll use in this program is list, random, shuffle
#multiple functions interaction and it's retun

example = [1,2,3,4,5,6,7]

from random import shuffle

shuffle(example)

#it will be shuffle and give output

#own version of shuffle by creating a def function

#function shuffle
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
result = shuffle_list(example)
result

#creating an game object ball or O using list
mylist = ['', 'O','']
shuffle_list(mylist)

#function for player guess
def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("pick a number 0, 1, or 2") #input always returns a string even if you enter integer
    retrun input(guess)

player_guess()
my_index = player_guess()

#OLD MACDONLAD: WRITE A function that caps the 1st and4th letter of a name

#old_mac('MACDONLAD') ==> MacDonald

def old_macdonald(name):
    firstletter = name[0]
    inbetween = name[1:3]
    fourth_letter = name[3]
    rest = name[4:]
    return firstletter.upper() + inbetween + fourth_letter + rest

    #reversing the words

    def rev_Word(text):
        wordList = text.split()
        rev_Word = wordList[::-1]
        return rev_Word
#has 33

def has_33(nums):
    for in n range (0, len(nums-1)):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

#challenging problem
#spyGame: write a function that takes a list of int and returns true  if it contains 007 in order
# spy_game([1,2,4,0,0,7,5]) --> True
# spy_game([1,0,2,4,0,5,7]) --> True
# spy_game([1,7,2,0,4,5,0]) -- False

def spy_game(nums):
    code = [0,0,7, 'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1

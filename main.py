# Python code to unscramble a jumbled word using the Enchant dictionary(US) and itertools in Python. 
from itertools import permutations
import enchant
word_list = enchant.Dict("en_US")

# Taking the input word and converting it into lowercase words. 
word = input("Enter the letters: ")
word = word.lower()
word_length = len(word)

# A function to print the unjumbled words according to the length of the word. 
def output_fnc(length):
    temp = []
    for word in ans:
        if len(word) == length:
            temp.append(word)
    if len(temp) != 0:
        print("Words of length " + str(length) + " are:")
        for temps in temp:
            print(temps)
    else:
        print("No words of length " + str(length))

# Variables to store the final correct words and to store all the possible permutations.
ans = []
perms = []

# Finding and adding all the permutations to the list.
for i in range(1, word_length + 1):
    for p in permutations(word, i):
        striing = ''
        len_p = len(p)
        for letter in range(0, len_p):
            striing += p[letter]
        perms.append(striing)

# Removing duplicates.
perms = list(set(perms))

# Checking if the permutation created is an actual English(US) word. 
for perm in perms:
    if word_list.check(perm):
        ans.append(perm)

#Printing the final results. 
for j in range(2, word_length + 1):
    output_fnc(j)


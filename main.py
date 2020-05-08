from itertools import permutations
import enchant
word_list = enchant.Dict("en_US")
word = input("Enter the letters: ")
word = word.lower()
word_length = len(word)
wordaslist = []

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

ans = []
perms = []

for i in range(1, word_length + 1):
    for p in permutations(word, i):
        striing = ''
        len_p = len(p)
        for letter in range(0, len_p):
            striing += p[letter]
        perms.append(striing)

perms = list(set(perms))

for perm in perms:
    if word_list.check(perm):
        ans.append(perm)

for j in range(2, word_length + 1):
    output_fnc(j)


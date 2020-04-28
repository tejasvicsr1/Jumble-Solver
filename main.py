import enchant
word_list = enchant.Dict("en_US")
word = input("Enter the letters: ")
word_length = len(word)
wordaslist = []

ans = []

for letter in range(0, word_length):
    wordaslist.append(word[letter])

# for i in range(2, (word_length + 1)):
for j in range(0, word_length):
    for k in range(0, word_length):
        temp = word[j] + word[k]
        if word_list.check(temp):
            ans.append(temp)

print(ans)
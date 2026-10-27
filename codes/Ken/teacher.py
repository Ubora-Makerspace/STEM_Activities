word = 'teacher'

word_1 = word[0:3]
word_2 = word[0:5]
word_3 = word[-3:-1]+ word[2] + word[-1]
word_4 = word[1:5]
word_5 = word[2:6]
word_6 = word[-3:-1]+ word[2] + word[-1] + word[0]
word_7 = word[-3:-1] + word[2] + word[0]
word_8 = word[0:3] + word[-1]

all_words = [word_1, word_2, word_3, word_4, word_5, word_6, word_7, word_8]
print(all_words)
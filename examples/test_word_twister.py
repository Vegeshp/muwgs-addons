from muwgs.application.word_twister import word_twister

s = 'abcdef'

for i in range(3, len(s) + 1):
    print(word_twister(s, i))

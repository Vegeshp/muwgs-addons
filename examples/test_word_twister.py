from muwgs.utils.keyboard_utils import word_press
from muwgs.application.word_twister import word_twister
from sys import path

path.append('..')

s = 'abcdef'

for i in range(3, len(s) + 1):
    for word in word_twister(s, i):
        word_press(word)

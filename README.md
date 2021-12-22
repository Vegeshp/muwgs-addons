# Microsoft Ultimate Word Games Addons

Python addons for playing "Microsoft Ultimate Word Games"

## Requirements

Windows 10 or above

pyenchant==3.2.2

pywin32==302

`Microsoft Ultimate Word Games` from *`Windows Store`*

## Documents

### muwgs.application.crosswords(s: str) -> List[str]

Given a format string of lower-case alphabets and '*', return all possible words

* Input

s: a string of lower-case alphabets and '*'

* Output

a list of possible words

### muwgs.application.word_twister(s: str, n: int) -> List[str]

Given a string of lower-case alphabets, return all possible words of length n with their permutations.

* Input

s: a string of lower-case alphabets

n: an integer representing desired length

* Output

a list of all possible words of length n with their permutations

### muwgs.application.wordament(s: str, press=True, print_result=False, n=4) -> List[str]

Given a string of n x n white-space-splited character/prefix/suffix/multi-character s, return all possible words by adjacent moves.

* Input

s: a string of n x n white-space-splited character/prefix/suffix/multi-character s

press: boolean value, represents whether results are pressed via keyboard

print_result: boolean value, stands for whether to print result or not

n: an integer for desired maximum length, setting to 7 to 8 for good performance

* Output

a list of possible words by adjacent moves

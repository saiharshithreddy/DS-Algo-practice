'''
You have a passage of text that needs to be typed out, but some of the letter representing the working letter keys, as well as a string text, and your keys on your keyboard are broken! You're given an array letters task is to determine how many of the words from text can be typed using the broken keyboard. It is guaranteed that all of the non-letter keys are working (including all punctuation and special characters).

A word is defined as a sequence of consecutive characters which does not contain any spaces. The given text is a string consisting of words, each separated by exactly one space. It is guaranteed that text does not contain any leading or trailing spaces.

Note that the characters in letters

are all lowercase, but since the shift key is working, it's possible to type the uppercase versions also.

Example

• For text - "Hello, this is CodeSignal!" and letters = ['e', 'i','h','l', 'o', 's'], the output should be brokenkeyboard(text,

letters) = 2

i. "Hello," can be typed since the characters 'h', 'e' , l' and 'o' are in letters. Note that the symbol , also belongs to the current word and can by typed.

ii. "this" cannot be typed because the character 't is not in letters.

iii. "is" can be typed (both 'i' and 's' appear in letters ).

iv. "CodeSignal!" cannot be typed because the character 'c is not in letters (as well as 'd', 'y', 'n', and 'a').

. For text = "Hi, this is Chris!" and letters = ['r', 's', 't', 'c', 'h'], the output should be brokenkeyboard(text, letters) = 0.

Each word contains the character 'i' which does not appear in letters and thus cannot be typed on the keyboard.

• For text = "3   2 = 5" and letters = 0, the output should be broken Keyboard(text, letters) = 5.

'''

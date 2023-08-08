#!/usr/bin/python3
for letter in range(97, 123):
    letter = chr(letter)
    if letter != 'q' and letter != 'e':
        print("{}".format(letter), end="")

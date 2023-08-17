#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    romanVls = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    romaN = 0
    for j in range(len(roman_string)):
        if j > 0 and romanVls[roman_string[j]] > romanVls[roman_string[j - 1]]:
            romaN += romanVls[roman_string[j]] - 2 * \
                        romanVls[roman_string[j - 1]]
        else:
            romaN += romanVls[roman_string[j]]
    return (romaN)

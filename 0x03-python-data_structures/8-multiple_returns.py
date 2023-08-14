#!/usr/bin/python3
"""
    If the sentence is empty, the first character should be equal to None
"""
def multiple_returns(sentence):
    if sentence == '':
        return (0, None)
    return (len(sentence), sentence[0])

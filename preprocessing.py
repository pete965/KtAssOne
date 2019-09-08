import numpy as np
import os
import string


def splitdictionary(capital):
    with open('dict.txt','r') as dictionary:
        data = dictionary.readlines()
        i = 0
        output = ""
        for line in data:
            if not len(line) == 0:
                if line[0] == capital:
                    output = output + line
    file = open('smallDictionary/dict'+capital+'.txt','w')
    file.write(str(output))


alphabet = "abcdefghijklmnopqrstuvwxyz"
for char in alphabet:
    splitdictionary(char)



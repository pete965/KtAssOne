import numpy as np
import os
import string
from pytrie import SortedStringTrie as Trie


# Split the dictionary file into smaller ones
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
    # alphabet = "abcdefghijklmnopqrstuvwxyz"
    # for char in alphabet:
    #     splitdictionary(char)


# Calculate the blender and its conponents maximum common prefix length and get the dictionary
def blendanalysis():
    with open('blends.txt','r') as blends:
        data = blends.readlines()
        max = 0
        dist = dict()
        for i in range(10):
            dist[i] = 0
        for line in data:
            out,in1,in2 = line.split("\t")
            i = 0
            local = 0
            localrev = 0
            for i in range(min(len(out),len(in1))):
                if out[i] == in1[i]:
                    local = local + 1
                else:
                    break
            i = 0
            for i in range(min(len(out),len(in2))):
                if out[i] == in2[i]:
                    localrev = localrev + 1
                else:
                    break
            if local < localrev:
                local = localrev
            dist[local] = dist[local] + 1
            if local > max:
                max = local
    with open('smallDictionary/blendAnalysis.txt','w') as bleAna:
        bl = ""
        all = 0
        for keys in dist.keys():
            bl = bl + str(keys) + ":" + str(dist[keys]) + "\n"
            all = all + dist[keys]
        for keys in dist.keys():
            bl = bl + str(keys) + ":" + str(dist[keys]/all) + "\n"
        bleAna.write(bl)


# Initiate an alphabate
def initalpha():
    dist = dict()
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for key in alpha:
        dist[key] = 0
    return dist


# Try to analysis blenders and figure out how many same characters will applear continuesly
# output: 2
def blendana():
    with open('blends.txt', 'r') as blends:
        data = blends.readlines()
        biggest = 0
        for line in data:
            blender = line.split("\t")[0]
            ls = []
            big = 0
            for key in blender:
                if not len(ls) == 0 and not key == ls[len(ls)-1]:
                    if len(ls) > big:
                        big = len(ls)
                    ls.clear()
                ls.append(key)
            if big > biggest:
                biggest = big
        print(biggest)

# blendana()


# give out a word's maximum continuous char
def getnumofcontinchar(word):
    ls = []
    big = 0
    for key in word:
        if not len(ls) == 0 and not key == ls[len(ls)-1]:
            if len(ls) > big:
                big = len(ls)
            ls.clear()
        ls.append(key)
    if len(ls) > big:
        big = len(ls)
    return big


def loaddictionary():
    dist = dict()
    with open('dict.txt','r') as dic:
        data = dic.readlines()
        for key in data:
            dist[key.split("\n")[0]] = 1
    return dist


alpha = "abcdefghijklmnopqrstuvwxyz"
# print(loaddictionary().get("a"))
# for key in alpha:
#     print(loaddictionary().get(key))
def getfirstn(word,n):
    return None


def getngram(word,dist):
    ls = []
    initial = word[0]
    length = len(word)
    words = dist[initial]
    if length > 4:
        for i in range(4):
            getfirstn(word,4-i)

    return ls

dist = loaddictionary()
# print("Load Complete")
def isindic(word):
    if word in dist[word[0]]:
        return True
    else:
        return False
# for key in alpha:
#     print(isindic(key))


def getprefix(word,length):
    prefix = ""
    for i in range(length):
        prefix = prefix + word[i]
    return prefix
#
#
# print(getprefix("swim",3))
# print(getprefix("apple",4))

dictionary = loaddictionary()
t = Trie(dictionary)
print(t.keys(prefix='ba'))
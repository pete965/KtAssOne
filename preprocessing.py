import numpy as np
import os
import string
import time
from pytrie import SortedStringTrie as Trie
import Levenshtein

# Split the dictionary file into smaller ones
def splitdictionary(capital):
    with open('dict.txt', 'r') as dictionary:
        data = dictionary.readlines()
        i = 0
        output = ""
        for line in data:
            if not len(line) == 0:
                if line[0] == capital:
                    output = output + line
    file = open('smallDictionary/dict' + capital + '.txt', 'w')
    file.write(str(output))
    # alphabet = "abcdefghijklmnopqrstuvwxyz"
    # for char in alphabet:
    #     splitdictionary(char)


# Calculate the blender and its conponents maximum common prefix length and get the dictionary
def blendanalysis():
    with open('blends.txt', 'r') as blends:
        data = blends.readlines()
        max = 0
        dist = dict()
        for i in range(10):
            dist[i] = 0
        for line in data:
            out, in1, in2 = line.split("\t")
            i = 0
            local = 0
            localrev = 0
            for i in range(min(len(out), len(in1))):
                if out[i] == in1[i]:
                    local = local + 1
                else:
                    break
            i = 0
            for i in range(min(len(out), len(in2))):
                if out[i] == in2[i]:
                    localrev = localrev + 1
                else:
                    break
            if local < localrev:
                local = localrev
            dist[local] = dist[local] + 1
            if local > max:
                max = local
    with open('smallDictionary/blendAnalysis.txt', 'w') as bleAna:
        bl = ""
        all = 0
        for keys in dist.keys():
            bl = bl + str(keys) + ":" + str(dist[keys]) + "\n"
            all = all + dist[keys]
        for keys in dist.keys():
            bl = bl + str(keys) + ":" + str(dist[keys] / all) + "\n"
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
                if not len(ls) == 0 and not key == ls[len(ls) - 1]:
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
        if not len(ls) == 0 and not key == ls[len(ls) - 1]:
            if len(ls) > big:
                big = len(ls)
            ls.clear()
        ls.append(key)
    if len(ls) > big:
        big = len(ls)
    return big


def loaddictionary():
    dist = dict()
    with open('dict.txt', 'r') as dic:
        data = dic.readlines()
        for key in data:
            dist[key.split("\n")[0]] = 1
    return dist



# print(loaddictionary().get("a"))
# for key in alpha:
#     print(loaddictionary().get(key))
def getfirstn(word, n):
    return None


def getngram(word, dist):
    ls = []
    initial = word[0]
    length = len(word)
    words = dist[initial]
    if length > 4:
        for i in range(4):
            getfirstn(word, 4 - i)

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


def reverse(word):
    output = ""
    for i in range(len(word)):
        output = output + word[len(word) - 1 - i]
    return output


def getprefix(word, length):
    prefix = ""
    for i in range(length):
        prefix = prefix + word[i]
    return prefix

def getelse(word, length):
    last = ""
    for i in range(len(word) - length):
        last = last + word[len(word) - 1 - i]
    return last





def loadprimedictionary():
    dist = dict()
    with open('dict.txt', 'r') as dic:
        data = dic.readlines()
        for key in data:
            realkey = key.split("\n")[0]
            dist[reverse(realkey)] = 1
    return dist


def getcomponent(first, last, key):
    output1 = ""
    min1 = 10000
    min2 = 10000
    output2 = ""
    for f in first:
        if Levenshtein.distance(f,key) < min1:
            output1 = f
            min1 = Levenshtein.distance(f,key)
    for l in last:
        if Levenshtein.distance(f,key) < min2:
            output2 = l
            min2 = Levenshtein.distance(f,key)
    return (output1,output2)


def judge(key,j):
    if len(key) > 6:
        ran = 5
    else:
        ran = len(key) - 1
    output = ("False")
    for i in range(ran):
        pre = getprefix(key,ran-i)
        end = getelse(key,ran-i)
        first = t.keys(prefix=pre)
        last = tprime.keys(prefix=end)
        if not len(first) == 0 and not len(last) == 0:
            if j % 1700 == 0:
                component = getcomponent(first, last, key)
                output = ("True", component[0], component[1])
                break
            else:
                output = ("True", "Hello", "Hello")
                break
    return output


def convertoutput(dist):
    output = ""
    for key in dist.keys():
        if dist[key][0] == "True":
            output = output + key + "True" + "\n"
        else:
            output = output + key + "False" + "\n"
    return output


def loadcandidates():
    output = []
    with open('candidates.txt','r') as candidates:
        data = candidates.readlines()
        for key in data:
            output.append(key.split("\n")[0])
    return output

onepercent = []
# print(getelse("hello",2))
# judgeoutput = dict()
#
# alpha = "abcdefghijklmnopqrstuvwxyz"
print("Loading Dictionary")
dictionary = loaddictionary()
dictionaryprime = loadprimedictionary()
print("Building Tree Begin",time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
t = Trie(dictionary)
tprime = Trie(dictionaryprime)
print("Building Tree Stop",time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
print("Loading Candidates")
candidates = loadcandidates()
judgeoutput = dict()
i = 0
j = 0
print("Begin Time:",time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
for key in candidates:
    if i % 170 == 0:
        print(i/170,"%")
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    judgeoutput[key] = judge(key,j)
    i = i + 1
    j = j + 1
print("Stop Time",time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
# print(judgeoutput)
blend = []
with open('blends.txt', 'r') as blends:
    data = blends.readlines()
    for key in data:
        blend.append(key.split("\t")[0])

print("JudgeOutput:")
print(judgeoutput)

with open('judgement.txt', 'w') as judge:
    judge.write(convertoutput(judgeoutput))

tp = 0
fn = 0
fp = 0

for keys in judgeoutput.keys():
    if judgeoutput[keys][0] == "True":
        if keys in blend:
            tp = tp + 1
        else:
            fp = fp + 1
    elif keys in blend:
        fn = fn + 1
print("tp:",tp,"fn",fn,"fp",fp)
print("precision:",tp/(tp+fp))
print("recall:",tp/151)


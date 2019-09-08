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


with open('blends.txt','r') as blends:
    data = blends.readlines()
    max = 0
    dist = dict()
    for i in range(10):
        dist[i] = 0
    for line in data:
        # print(line)
        out,in1,in2 = line.split("\t")
        stop = False
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
        # if local == 0:
            # print("#################")
            # print(out)
            # print(in1)
            # print(in2)
            # print("#################")
        if local > max:
            max = local
            # print(out)
            # print(in1)
            # print(in2)
        local = 0
    # print(max)
    # print(dist)

with open('smallDictionary/blendAnalysis.txt','w') as bleAna:
    bl = ""
    for keys in dist.keys():
        bl = bl + str(keys) + ":" + str(dist[keys]) + "\n"
    print(bl)
    bleAna.write(bl)

# alphabet = "abcdefghijklmnopqrstuvwxyz"
# for char in alphabet:
#     splitdictionary(char)
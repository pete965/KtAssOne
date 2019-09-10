# def convertoutput(dist):
#     output = ""
#     for key in dist.keys():
#         output = output + key + str(dist[key][0]) + "\n"
#     return output
#
# dist = {"a":(1,2),"aa":(1,2),"sss":(1,2),"bab":(1,2),"ba":(1,2),"banana":(1,2),"sss":(1,2),"ccc":(1,2),"eee":(1,2),"s":(1,2),"xxx":(1,2),"x":(1,2),"x":(1,2)}
# print(convertoutput(dist))


def reverse(word):
    output = ""
    for i in range(len(word)):
        output = output + word[len(word) - 1 - i]
    return output


def getelse(word, length):
    last = ""
    for i in range(len(word) - length):
        last = last + word[len(word) - 1 - i]
    return last

print(getelse("Hello",3))
print(getelse("banana",1))
print(reverse(getelse("Hello",3)))
print(reverse(getelse("banana",1)))
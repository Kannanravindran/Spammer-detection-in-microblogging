import json
import ast
import unicodedata
def byteify(input):
    if isinstance(input, dict):
        return {byteify(key):byteify(value) for key,value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input
inFile = open('biibbble.json', 'r')
temp = inFile.read()
temp1  = temp.lstrip('[').rstrip(']')
dict1 = ast.literal_eval(temp1)
dictRes = {}
dictRes = byteify(dict1[0])
outFile = open('testData.txt','wb')
outFile.write(str(dict1[0]))
outFile.write('\n\n')
outFile.write(str(dictRes))

import json
import ast
import unicodedata
import os

def toString(input):
    if isinstance(input, dict):
        return {toString(key):toString(value) for key,value in input.iteritems()}
    elif isinstance(input, list):
        return [toString(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

input_files = [filename for filename in os.listdir(".") if filename.endswith(".json")]

for filename in input_files:
	in_file = open(filename, 'r')
	content = in_file.read()
	content  = content.lstrip('[').rstrip(']')
	input_dicts = ast.literal_eval(content)

	string_converted = ()
	for item in range(len(input_dicts)):
		string_converted[item] = toString(input_dicts[item])

	out_file = open(filename.rstrip('.json')+'_string.py','wb')
	out_file.write(str(string_converted))

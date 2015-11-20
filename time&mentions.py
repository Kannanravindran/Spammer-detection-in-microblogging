import importlib
import os
import datetime as dt
from datetime import date
import time

def extract_replies():
	input_files = [filename for filename in os.listdir('.') if filename.endswith("_string.py")]
	for filename in input_files:
		file_object = importlib.import_module(filename.rstrip('.py'))
		content = file_object.content
	return content


def timediff(content):
	temp = 0.0
	for x in content:
		d1 = x['created_at']
		d1 = time.strptime(d1,'%a %b %d %H:%M:%S +0000 %Y')
		d1 = time.mktime(d1)
		diff = abs(d1 - temp)
		print diff
		temp = d1

def mentions(content):
	mentions = 0
	total = 0
	# term = '@'
	for x in content:
		tweet = x['text']
		for word in tweet.split():
			if word.startswith('@'):
				mentions = mentions + 1
	print 'Mentions:',mentions
	print 'Total tweets:', len(content) 

content = extract_replies()
timediff(content)
mentions(content)

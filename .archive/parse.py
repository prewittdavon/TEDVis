import os
from os import listdir
from os.path import isfile, join, isdir
from operator import itemgetter, attrgetter
from wiki import filter
from string import punctuation
from nltk.corpus import wordnet as wn



wordDict = {}

def countWords():
	onlyfiles = [f for f in listdir(".") if isfile(join(".", f))]

	#print(onlyfiles)
	#wordDict = {}
	for file in onlyfiles:
		with open(file) as f:
			lines = f.readlines()
			for line in lines:
				line = line.split()
				for word in line:
					word = word.lower()
					strip_punctuation(word)
						#print(word + " " + tmp[0].pos())
					if word not in wordDict:
						wordDict[word] = 0

					wordDict[word] += 1

def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)


path = os.getcwd() + '/TEDVis'
os.chdir(path)
tedTypes = [f for f in listdir(".") if  isdir(join(".", f)) and not f.startswith('.')]
#print(os.getcwd())
for folder in tedTypes:
	#print(os.getcwd())
	os.chdir(folder)
	alphabet = [f for f in listdir(".") if  isdir(join(".", f)) and not f.startswith('.')]
	print(os.getcwd())
	for group in alphabet:
		os.chdir(group)

		#print(os.getcwd())
		countWords()
		os.chdir('..')

	os.chdir('..')
		# os.chdir(folder)
		# print(os.listdir('.'))
		#onlydirs = [f for f in listdir(".") if  isdir(join(".", f))]
		#os.chdir('..')

filter(wordDict)
wordList = []
adjList = []

for key in wordDict:
	tmp = wn.synsets(key)
	if (len(tmp) > 0):
		if (tmp[0].pos() == "a"):
			adjList.append({"word": key, "frequency": wordDict[key]})

adjList = sorted(adjList, key=itemgetter("frequency"), reverse = True)

print(adjList)

# print(len(wordList))

import json
with open('data.json', 'w') as outfile:
    json.dump(adjList[:10], outfile)





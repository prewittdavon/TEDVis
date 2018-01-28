

from os import listdir
import os
from os.path import isfile, join
from operator import itemgetter, attrgetter


def getWords()
	onlyfiles = [f for f in listdir(".") if isfile(join(".", f))]

	#print(onlyfiles)
	#wordDict = {}
	for file in onlyfiles:
		with open(file) as f:
			lines = f.readlines()
			for line in lines:
				line = line.split()
				for word in line:
					if word not in wordDict:
						wordDict[word] = 0
					wordDict[word] += 1
	wordList = [] 
	for key in wordDict:
		wordList.append((wordDict[key], key))

	wordList = sorted(wordList, key=itemgetter(0), reverse = True)
	print(wordList)




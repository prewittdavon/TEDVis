import requests
#Next we will use requests.get to retrieve the web page with our data, parse it using the html module and save the results in tree:

def filter(wordDict):
	page = requests.get('https://en.wikipedia.org/wiki/Most_common_words_in_English')
	text = page.text.split('wikt:')[1:]
	for i in range(len(text)):
		text[i] = text[i][:text[i].find("\"")]
		wordDict.pop(text[i], None)
		#print(text[i])
	# words = text
	# return words
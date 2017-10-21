import pickle
import math
# This function is called for training only
def readAndStore(file):
	with open(file,"r") as f:
		f=f.read().splitlines()
		for line in f:
			city=line.split(" ")[0]
			if city in bagOfWords.keys():
				cityCount[city]=cityCount[city]+1
				for word in line.split(" ")[1:]:
					if word in bagOfWords[city].keys():
						bagOfWords[city][word]=bagOfWords[city][word]+1
						wordCount[word]=wordCount[word]+1
					else:
						bagOfWords[city][word]=1
						wordCount[word]=1
			else:
				cityCount[city]=1
				bagOfWords[city]={}
				for word in line.split(" ")[1:]:
					if word in bagOfWords[city].keys():
						bagOfWords[city][word]=bagOfWords[city][word]+1
						wordCount[word]=wordCount[word]+1
					else:
						bagOfWords[city][word]=1
						wordCount[word]=1
	w=open("bagOfWords.txt", "w")
	w.write(str(bagOfWords))
	w=open("wordCount.txt", "w")
	w.write(str(wordCount))
	w=open("cityCount.txt", "w")
	w.write(str(cityCount))
	pickle.dump(bagOfWords,open("bagOfWords.p", "wb"))
	pickle.dump(wordCount,open("wordCount.p", "wb"))
	pickle.dump(cityCount,open("cityCount.p", "wb"))

#This function finds P(City|W1....Wn)=(P(W1.....Wn|City)*P(City))/P(W1.....Wn)
def probabilityCityGivenWords(citywordspair):
	city=citywordspair[0]
	words=citywordspair[1]
	#need to make changes here
	probability=float(probabilityCity(city))
	# to here
	for word in words:
		a=probabilityWordGivenCity(city,word)
		#b=probabilityWord(word)
		if a!=0: #and b!=0:
			probability=probability+float(a/b)
		else:
			probability=probability+0
	return float(probability)

#This function finds P(W1.....Wn|City)
def probabilityWordGivenCity(city,word):
	if word in bagOfWords[city].keys():
		return float(bagOfWords[city][word]/sum(bagOfWords[city].values()))
	else:
		return 0

#This function finds P(City)
def probabilityCity(city):
	#print sum(cityCount.values()[:])
	return float(cityCount[city]/sum(cityCount.values()))

#This function finds P(W1.....Wn)
def probabilityWord(word):
	if word in wordCount.keys():
		return float(wordCount[word]/sum(wordCount.values()))
	else:
		return 0
#No need to change this. Main changes is probabilitycitygivewords
def predict(file):
	with open(file,"r") as f:
		f=f.readlines()
		for line in f:
			answerCity=line.split(" ")[0]
			#print answerCity
			words=line.split(" ")[1:]
			#print "\n",words
			citywordspair=[]
			for city in cityCount.keys():
				citywordspair.append([city,words])
			predictedCity=max(citywordspair,key=probabilityCityGivenWords)[0]
			predictedScore=probabilityCityGivenWords([predictedCity,words])
			print "The answer is:",answerCity," and the prediction is:",predictedCity," with a score of",predictedScore

bagOfWords={}
wordCount={}
cityCount={}
#readAndStore("tweets.train.txt")
bagOfWords=pickle.load(open("bagOfWords.p","rb"))
wordCount=pickle.load(open("wordCount.p","rb"))
cityCount=pickle.load(open("cityCount.p","rb"))
#print bagOfWords.keys()
print cityCount.keys()
#print bagOfWords
#print sum(bagOfWords['Washington,_DC'].values())
predict("tweets.test1.txt")
#print sum(cityCount.values())

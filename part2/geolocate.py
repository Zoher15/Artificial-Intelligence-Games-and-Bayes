#!/usr/bin/env python
#Assignment 2 Question 2 "Testing loctation of Tweets" Elements of Artificial Intelligence by David Crandall
#Author: Zoher Kachwala
'''
I tried many different things:
1. By summing the individual probabilities of a word in a tweet than the product (to get around the problem of 0 probability) when a word doesnt occur
2. By giving more weight to words in a tweet for ocurring in the top 5 words of a city
3. Tried all sorts of small values for a word that has never occured given a city before finally settled on (1/100000)
4. Keep the uppercase, punctuation (gave slow speeds due to large dictionary sizes)
5. Scanning all words of every length
6. Scanning only words of length 1-10 (settled on length 5 for the highest accuracy) but I also did not want to lose on scanning initials
of states like: NY, MA, CA and so on
Preserving the elements of the city name and state is very important as the training set may not contain tweets explicitly with 'NY','MA','CA'
but while testing it should still use those important city and state names for prediction. It is absolutely essential to predict the location of the city correctly
if the test tweet contains the state or city name. Failing just because the training tweets did not contain it, would be a dumb classifier.
That is why I have done my best to not ignore the names of city and their states by dictionaries and lists called cityRelatedWords{} and cityRelatedWordsList[]

For the given training (tweets.train.txt) and test (tweets.test1.txt) files my code runs in 21 seconds on burrow and predicts with an accuracy of 68%
'''
import math
import re
import string
import operator
import sys
# This function for training and building initial dictionaries bagOfWords and cityCount
def readAndStore(file):
	with open(file,"r") as f:
		f=f.readlines()
		for line in f:
			city=line.split(" ")[0]
			line=re.findall(r"[\w']+",line)#regex for storing group of characters from a-z, basically resulting in words
			line = filter(lambda x: len(x) > 5 or x in city.split(',_'), line)#found with experimentation that skipping words of length 5 or less helps accuracy
			#the second condition is to not filter few exception like NY,CA and so on which are present in city name which are shorter than 5 but important
			if city in bagOfWords.keys():
				cityCount[city]=cityCount[city]+1
				for word in line:
					word=word.lower()
					if word in bagOfWords[city].keys():
						bagOfWords[city][word]=bagOfWords[city][word]+1
					else:
						bagOfWords[city][word]=1
			else:
				cityCount[city]=1
				bagOfWords[city]={}
				for word in line:
					word=word.lower()
					if word in bagOfWords[city].keys():
						bagOfWords[city][word]=bagOfWords[city][word]+1
					else:
						bagOfWords[city][word]=1

#This function is used to test the input file
def predict(file):
	answerCity=[]
	predictedCity=[]
	wordsline=[]
	with open(file,"r") as f:
		f=f.readlines()
		for line in f:
			wordsline.append(line)
			answerCity.append(line.split(" ")[0])
			words=re.findall(r"[\w']+",line)#regex for storing group of characters from a-z, basically resulting in words
			words = filter(lambda x: x in cityRelatedWordsList or len(x) > 5, words)#found with experimentation that skipping words of length 5 or less helps accuracy
			#the second condition is to not filter few cityRelatedWords like NY,CA and so on which are present in city name
			words=words[1:]
			citywordspair=[]
			for city in cityCount.keys():
				citywordspair.append([city,words])
			predictedCity.append(max(citywordspair,key=probabilityCityGivenWords)[0])
	accuracy(answerCity,predictedCity,wordsline,outputfile)

#This function finds P(City|W1....Wn)=(P(W1.....Wn|City)*P(City))
def probabilityCityGivenWords(citywordspair):
	city=citywordspair[0]
	words=citywordspair[1]
	probability=probabilityCity(city)#P(City)
	for word in words:
		word=word.lower()
		probability=probability+probabilityWordGivenCity(city,word)#P(W1.....Wn|City)
	return float(probability)

#This function finds P(W1.....Wn|City) from the bagofwords dictionary
def probabilityWordGivenCity(city,word):
	if word in bagOfWords[city].keys():
		return math.log(bagOfWords[city][word])-math.log(sum(bagOfWords[city].values()))
	else:
		return math.log(1)-math.log(100000)

#This function finds P(City)
def probabilityCity(city):
	return math.log(cityCount[city])-math.log(sum(cityCount.values()))
#funtion to find acccuracy and write the accuracy to output file
def accuracy(answerCity,predictedCity,wordsline,file):
	correct=0
	with open(file,"w") as f:
		for i in range(len(wordsline)):
			f.write(predictedCity[i]+" "+wordsline[i])

#function to find and store top words to a dictionary topWordsGivenCity
def topWords():
	for city in bagOfWords.keys():
		topWordsGivenCity[city]=sorted(bagOfWords[city].items(),key=operator.itemgetter(1),reverse=True)[:5]
		topWordsGivenCity[city]= {x[0]:x[1] for x in topWordsGivenCity[city]}

trainingfile=sys.argv[1]
testingfile=sys.argv[2]
outputfile=sys.argv[3]
bagOfWords={}#Dictionary to store word given city relation
cityCount={}#Dictionary to store count of tweets with a particular city
cityRelatedWords={}#Dictionary to store words in the the string of city name
topWordsGivenCity={}#Dictionary to store top occurring words of a particular city
cityRelatedWordsList=[]#Dictionary to store all words that are shorter than length 5 but essential like NY,CA so on
readAndStore(trainingfile)
cityRelatedWords={x:x.split(",_") for x in cityCount.keys()}
#to create a list combining all cityrelated words that maybe less than length 5 to not skip them while reading
for city in cityRelatedWords.keys():
	for word in cityRelatedWords[city]:
		cityRelatedWordsList.append(word)
topWords()
predict(testingfile)
#for printing city and their top words
for city in topWordsGivenCity.keys():
	print "\n",city,":",
	for word in topWordsGivenCity[city]:
		print word,

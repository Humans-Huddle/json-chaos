import json
from pprint import pprint
import re
import csv
import json
import urllib2
import itertools
import codecs


###     extract tweets from archive     ###

json_data=open('Human-Security.json')
data = json.load(json_data)

#store tweet text as CSV
outfile = 'tweets'".csv"
myfile = codecs.open(outfile, "wb", 'utf-8')
w = csv.writer(myfile)
for i in range(len(data['statuses'])):
    w.writerow(codecs.unicode_escape_encode(data['statuses'][i]['text']))
myfile.close()



###     Most Mentioned users    ###

#find all @mentions in tweet text - and store as csv
outfile = 'mentions1'".csv"
myfile = codecs.open(outfile, "wb", 'utf-8')
w = csv.writer(myfile)
input = codecs.open('tweets.csv', "r", 'utf-8')
text = input.read()
regex = "(?=(@[\w]+))"
for result in re.finditer(regex, text):
    w.writerow(codecs.unicode_escape_encode("".join(result.groups())))
myfile.close()

# open list of people mentioned
input = open('mentions1.csv', 'r')
text = input.read()
wordlist = text.split()

#frequency of people mentioned
outfile = 'mentionsfrequency'".csv"
myfile = open(outfile, "wb")
w = csv.writer(myfile)

wordfreq = [wordlist.count(p) for p in wordlist]
dictionary = dict(zip(wordlist,wordfreq))
aux = [(dictionary[key], key) for key in dictionary]
aux.sort()
aux.reverse()
for a in aux: w.writerow(a)
myfile.close()


###     frequent tags in tweets    ###

# #tags in tweets and store as csv (utf-8)

outfile = 'tagslist'".csv"
myfile = codecs.open(outfile, "wb", 'utf-8')
w = csv.writer(myfile)
input = codecs.open('tweets.csv', "r", 'utf-8')
text = input.read()
regex = "(?=(#[\w]+))"
for result in re.finditer(regex, text):
    w.writerow(codecs.unicode_escape_encode("".join(result.groups())))
myfile.close()


#Open list of tags
input = codecs.open('tagslist.csv', "r", 'utf-8')
text = input.read()
wordlist = text.split()


#frequency of tags used
outfile = 'tagfrequency'".csv"
myfile = codecs.open(outfile, "wb", 'utf-8')
w = csv.writer(myfile)

wordfreq = [wordlist.count(p) for p in wordlist]
dictionary = dict(zip(wordlist,wordfreq))
aux = [(dictionary[key], key) for key in dictionary]
aux.sort()
aux.reverse()
for a in aux: w.writerow(a)
myfile.close()


###     Frequent Tweeters store as CSV   ###

#open archive
json_data=open('Human-Security.json')
data = json.load(json_data)

#find users
outfile = 'users'".csv"
myfile = open(outfile, "wb")
w = csv.writer(myfile)
for i in range(len(data['statuses'])):
    w.writerow([data['statuses'][i]['user']['screen_name']])
myfile.close()

#Find frequency of users
input = open('users.csv', 'r')
text = input.read()
wordlist = text.split()

outfile = 'usersfrequency'".csv"
myfile = open(outfile, "wb")
w = csv.writer(myfile)

wordfreq = [wordlist.count(p) for p in wordlist]
dictionary = dict(zip(wordlist,wordfreq))
aux = [(dictionary[key], key) for key in dictionary]

#sort for most frequent
aux.sort()
aux.reverse()
for a in aux: w.writerow(a)
myfile.close()

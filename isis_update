import json
from pprint import pprint
import re
import csv
import json
import urllib2
import itertools
import codecs


            ###     Build data set - extract tweets from archive     ###

json_data=open('insecurity.json')
data = json.load(json_data)

#store tweet text as CSV
outfile = 'tweets'".csv"
myfile = codecs.open(outfile, "wb", 'utf-8')
w = csv.writer(myfile)
for i in range(len(data['statuses'])):
    w.writerow(codecs.unicode_escape_encode(data['statuses'][i]['text']))
myfile.close()



                           ### ANALYSIS SECTION ###



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


                  ###     FREQUENT TAGS IN TWEETS     ###

# #tags in tweets and store as csv (utf-8)

outfile = 'tagslist'".csv"
myfile = codecs.open(outfile, "wb", 'utf-8')
w = csv.writer(myfile)
input = codecs.open('tweets.csv', "r", 'utf-8')
text = input.read()
lexi = text.lower()
regex = "(?=(#[\w]+))"
for result in re.finditer(regex, lexi):
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




                ###     FREQUENT LINKS IN TWEETS ###


json_data=open('insecurity2.json')
data = json.load(json_data)

#store tweet text as CSV
outfile = 'tweets_nonUTF'".csv"
myfile = codecs.open(outfile, "wb",)
w = csv.writer(myfile)
for i in range(len(data['statuses'])):
    w.writerow(codecs.unicode_escape_encode(data['statuses'][i]['text']))
myfile.close()


outfile = 'linkslist'".csv"
myfile = codecs.open(outfile, "wb", 'utf-8')
w = csv.writer(myfile)
input = codecs.open('tweets.csv', "r", 'utf-8')
text = input.read()
links_regex = "(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)"
for result in re.finditer(links_regex, text):
    w.writerow(codecs.unicode_escape_encode("".join(result.groups())))
myfile.close()


#Open list of Links
input = codecs.open('linkslist.csv', "r", 'utf-8')
text = input.read()
wordlist = text.split()


#frequency of tags used
outfile = 'links_frequency'".csv"
myfile = codecs.open(outfile, "wb", 'utf-8')
w = csv.writer(myfile)

wordfreq = [wordlist.count(p) for p in wordlist]
dictionary = dict(zip(wordlist,wordfreq))
aux = [(dictionary[key], key) for key in dictionary]
aux.sort()
aux.reverse()
for a in aux: w.writerow(a)
myfile.close()



                    ### MOST ACTIVE USERS ###


###     Frequent Tweeters store as CSV   ###

#open archive
json_data=open('insecurity2.json')
data = json.load(json_data)

#find users
outfile = 'users'".csv"
myfile = open(outfile, "a")
w = csv.writer(myfile)
for i in range(len(data['statuses'])):
    try:
        w.writerow([data['statuses'][i]['user']['screen_name']])
    except KeyError:
        print 'error'
  		#Regular expression for getting @mentions
    else:
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

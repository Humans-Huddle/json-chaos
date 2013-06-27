from urlunshort import resolve
import httplib
import urlparse
import csv

#list of shortlinks:
urls = ['http://zite.to/12Uq1nW'
]

#store file
outfile = 'longlinks'".csv"
myfile = open(outfile, "wb",)
w = csv.writer(myfile)



for url in urls:
    results = []
    results += [resolve(url)]
    w.writerow(results)

myfile.close()



import httplib
import urlparse
import csv

#list of shortlinks:
url = ['http://t.co/uBFlnqZ0YU'
]

#store file
outfile = 'longlinks'".csv"
myfile = open(outfile, "wb",)
w = csv.writer(myfile)

def unshorten_url(url):
    parsed = urlparse.urlparse(url)
    h = httplib.HTTPConnection(parsed.netloc)
    resource = parsed.path
    if parsed.query != "":
        resource += "?" + parsed.query
    h.request('HEAD', resource )
    response = h.getresponse()
    if response.status/100 == 3 and response.getheader('Location'):
        return unshorten_url(response.getheader('Location')) # changed to process chains of short urls
    else:
        return url

for row in [url]:
    print expand-shorlinks.unshorten_url()


myfile.close()



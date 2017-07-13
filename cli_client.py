import urllib2

req = urllib2.Request("http://127.0.0.1:5000/cpu")
response = urllib2.urlopen(req)
the_page = response.read()

print(the_page)

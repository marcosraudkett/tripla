import urllib.request
e = "e" 
n = "n"
l = "l"
a = "a"
p = "p"
s = "s"
r = "r"

start = 1571054404 #the first image

i = 1
while i < 25000000:																 
	
	URL = "http://frames10." + e+n+l+a+p+s+e+r + ".cloud/85956142/fi/frame_service/?timestamp=" + str(start) + "000"
	try:
		urllib.request.urlretrieve(URL, "images/" + str(start) + ".jpg")
	except urllib.error.HTTPError as err:
   		if err.code == 404:
   			print("404-skipping-" + str(start) + ": " + URL)

	
	start = start + 1 * 60 * 60 # add 1+ hour to unix time
	print(start)
	i += 1

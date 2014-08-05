import re
import requests
import pickle
import time

ystart = 1827
yend = 2014



limits = {}
for year in xrange(ystart,yend+1):
  time.sleep(5)
  print "Doing "+str(year)
  r = requests.get("http://mnras.oxfordjournals.org/content/by/year/"+str(year))
  if r.status_code != requests.codes.ok:
    print "Request Error"
    print r.content
    continue
  for line in r.text.split("\n"):
    result = re.search('(\d+)[ (]+(\d+)\D*page-range\D*(\d+)[ -]+(\d+)',line)
    if result:
      volume = result.group(1)
      issue = result.group(2)
      pstart = result.group(3)
      pend = result.group(4)
      if volume not in limits:
        limits[volume] = {}
      limits[volume][issue] = [int(pstart), int(pend)]

out = open("mnras_limits.p","w")
pickle.dump(limits,out);

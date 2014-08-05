import re
import requests
import pickle
import time

vstart = 471
vend = 791
#vstart = 790
#vend = 790


limits = {}
for volume in xrange(vstart,vend+1):
  volume = str(volume)
  time.sleep(5)
  print "Doing volume "+volume
  r = requests.get("http://iopscience.iop.org/0004-637X/"+volume)
  if r.status_code != requests.codes.ok:
    print "Request Error"
    print r.content
    continue
  #for line in r.text.split("\n"):
  for result in re.finditer("/0004-637X/"+volume+"/(\d+).*?\((\d+)[ -]+(\d+)\)",r.text,re.DOTALL):
    if volume not in limits:
      limits[volume] = {}
    issue = str(result.group(1))
    pstart = result.group(2)
    pend = result.group(3)
    limits[volume][issue] = [int(pstart), int(pend)]

#print limits
out = open("apj_limits.p","w")
pickle.dump(limits,out);
out.close()

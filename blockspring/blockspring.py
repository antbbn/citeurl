import re
import sys
import requests


class mnras:
  # MNRAS
  #usually need only the start page
  #issue is never in the citation, must be guessed/ spit all of them (usually under 4)
  fields = ['volume','page']
  patterns = [ 
              "MNRAS[, ]+(?P<volume>\d+)[, ]+(?P<page>\d+)",
              "Mon[. ]+Not[. ]+Roy[. ]+Astron[. ]+Soc[. ,]+(?P<volume>\d+)[, ]+(?P<page>\d+)",
              "Mon[. ]+Not[. ]+Roy[. ]+Astron[. ]+Soc[. ,]+(?P<volume>\d+)[, (]+(?P<year>\d+)[ ),]+(?P<page>\d+)",
            ]


  def urls(self):
    for issue in xrange(1,5):
      url =  "http://mnras.oxfordjournals.org/content/{volume}/{issue}/{page}.abstract".format(volume=self.volume,issue=issue,page=self.page)
      r = requests.get(url)
      if r.status_code == requests.codes.ok:
	return r.url
    return None

class prd:
  #Phys rev D 
  # typical url: https://journals.aps.org/prd/abstract/10.1103/PhysRevD.37.3406
  # the 10.1103 comes from the doi
  fields = ['issue','papid']
  patterns = [
              "Phys[. ]+Rev[. ]+D[ ,]*(?P<issue>\d+)[, (]+(?P<year>\d+)[ ),]+(?P<papid>\d+)",
              "Phys[. ]+Rev[. ]+D[ ,]*(?P<issue>\d+)[, ]+(?P<papid>\d+)",
            ]

  def urls(self):
    url =  "http://journals.aps.org/prd/abstract/10.1103/PhysRevD.{issue}.{papid}".format(issue=self.issue,papid=self.papid)
    return url



def match(obj, cit):
  for pattern in obj.patterns:
    result = re.search(pattern,cit)
    if result:
      [setattr(obj,field,result.group(field)) for field in obj.fields]
      return True
  return False

sources = [mnras,prd]

for source in sources:
  obj = source()
  if match(obj," ".join(sys.argv[1:])):
    url = obj.urls()
    if url:
      print '<a target="_blank" href="'+url+'">'+url+'</a>'
    else:
      print 'No link found'
    break
else:
  print 'No link found'
  

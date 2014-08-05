import pickle

class matcher:
  # MNRAS
  #usually need only the start page
  #issue is never in the citation, must be guessed/ spit all of them (usually under 4)
  fields = ['volume','page']
  patterns = [ 
              "MNRAS[, ]+(?P<volume>\d+)[, ]+(?P<page>\d+)",
              "Mon[. ]+Not[. ]+R[oy. ]+Astron[. ]+Soc[. ,]+(?P<volume>\d+)[, ]+(?P<page>\d+)",
              "Mon[. ]+Not[. ]+R[oy. ]+Astron[. ]+Soc[. ,]+(?P<volume>\d+)[, (]+(?P<year>\d+)[ ),]+(?P<page>\d+)",
            ]


  def urls(self):
    issue = self.get_issue()
    if issue is not None:
      url =  "http://mnras.oxfordjournals.org/content/{volume}/{issue}/{page}.abstract".format(volume=self.volume,issue=issue,page=self.page)
      return url
    else:
      return None

  def get_issue(self):
    file = open("sources/util/mnras/mnras_limits.p","rb");
    limits = pickle.load(file)
    if self.volume in limits:
      for issue, range in limits[self.volume].iteritems():
        if range[0] <= int(self.page) <= range[1]:
          return issue
    return None

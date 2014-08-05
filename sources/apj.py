import pickle

class matcher:
  # Astrophysical Journal
  #issue is never in the citation, must be guessed/ spit all of them (usually under 4)
  fields = ['volume','page']
  patterns = [ 
              "ApJ[. ,]+(?P<volume>\d+)[, ]+(?P<page>\d+)",
              "Astrophys[. ,J]+(?P<volume>\d+)[, ]+(?P<page>\d+)",
            ]


  def urls(self):
    issue = self.get_issue()
    if issue is not None:
      url = "http://iopscience.iop.org/0004-637X/{volume}/{issue}/{page}".format(volume=self.volume,issue=issue,page=self.page)
      return url
    else:
      return None

  def get_issue(self):
    file = open("sources/util/apj/apj_limits.p","rb");
    limits = pickle.load(file)
    if self.volume in limits:
      for issue, range in limits[self.volume].iteritems():
        if range[0] <= int(self.page) <= range[1]:
          return issue
    return None

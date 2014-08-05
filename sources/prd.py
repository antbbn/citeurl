class matcher:
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


class matcher:
  # JCAP
  #issue is never in the citation, must be guessed/ spit all of them (usually under 4)
  fields = ['year','month','papid']
  patterns = [ 
              "(?P<year>\d+)[, ]+Journal of Cosmology and Astro-Particle Physics[, ]+(?P<month>\d+)[, ]+(?P<papid>\d+)",
              "(?P<year>\d+)[, ]+JCAP[, ]+(?P<short_year>\d\d)(?P<month>\d\d)[, ]+(?P<papid>\d+)",
              "JCAP[, ]+(?P<month>\d+)[, (]+(?P<year>\d+)[), ]+(?P<papid>\d+)",
            ]


  def urls(self):
    url = "http://iopscience.iop.org/1475-7516/{year}/{month:>02}/{papid:>03}".format(year=self.year,month=self.month,papid=self.papid)
    return url

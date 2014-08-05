import re
import sys

import sources

def match(obj, cit):
  for pattern in obj.patterns:
    result = re.search(pattern,cit)
    if result:
      [setattr(obj,field,result.group(field)) for field in obj.fields]
      return True
  return False


for source in sources.list:
  obj = source()
  if match(obj," ".join(sys.argv[1:])):
    print obj.urls()
    break

import sys
import urllib2


url = sys.argv[1]

print "Testing: ", url

try: 
  response = urllib2.urlopen(url)
  html = response.read()

  #if html.find('indianred') == -1:
  #  print "Fail: we expect ** indianred ** color in <H1>"
  #  sys.exit(1)
except urllib2.URLError as e:
  print "Fail:",  e.reason
  sys.exit(1)

    
print "Test Passing Successfully"

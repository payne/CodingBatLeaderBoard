from bs4 import BeautifulSoup

class Problem:
  def __init__(self, img, a):
    self.img = img
    self.a = a

  def __str__(self):
    #return "eggs" # self.img.attrs['src]' + " <---> " + self.a.attrs['href'] + self.a.text
    try:
      return "(%s,%s,%s)" % (self.img.attrs['src'], self.a.attrs['href'], self.a.text)
    except KeyError:
      return ""



html_doc="""

"""


soup = BeautifulSoup(html_doc, 'html.parser')

#print(soup.prettify())
#print(soup.script)
a = soup.find_all('a')
print(a[20])
ps = a[20].findPreviousSibling()
print(ps)
for p in a:
  ps = p.findPreviousSibling()
  if (ps!= None):
    prob = Problem(ps, p)
    print(prob)



import urllib2
import re

def saveFile(url, fileName):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    with open(fileName,'wb') as handle:
        handle.write(response.read())
        print 'downloading %s ...' %fileName

def main():
    base_url = 'https://www.electroimpact.com/Whitepapers/'
    page = 'https://www.electroimpact.com/Whitepapers.aspx'
    request = urllib2.Request(page)
    response = urllib2.urlopen(request)
    url_lst = re.findall('<a href.*?/WhitePapers/(.*\.pdf).*?</a>', response.read())
    print '%d PDFs are found. Now downloading...' %(len(url_lst))
    for url in url_lst:
        fileName = url
        url = base_url + url
        saveFile(url, fileName)
        
main()



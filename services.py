from bs4 import BeautifulSoup
import requests
import urllib2
global size
global domain

    
def correcturl(url):
    #google.com
    #www.google.com
    
    if url[:4:] != 'http':
        url = 'http://' + url
    return url
    
def page_size(page,url):
    try:
        size = int(page.headers['content-length'])    
    except:
        size = len(urllib2.urlopen(url).read())
    print 'page_size-->',size,'bytes'


def link_count(page,url, debug=False):

    domain=url.split('//')[1]   #extracting domain of input url 
    count=0
    soup = BeautifulSoup(page.text,'lxml')
    for links in soup.find_all("a"):
        if links.has_attr("href"):
            links_list = links.attrs['href'].split('/')   
            try:    
                if domain in links_list[2]:
                    if debug==True:                 #if condition is false
                        print links.attrs['href']
                    count+=1
            except:
                pass
        
    print 'link_counts-->',count
    

            
url=raw_input('Enter the url: ')
try:
    url = correcturl(url)
    page=requests.get(url)
    link_count(page,url)
    page_size(page,url)
except:                     #for any invalid input url
    print 'invalid URL'

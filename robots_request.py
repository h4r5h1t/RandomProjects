import requests
from furl import furl
import re 

urls = ['https://www.breachlock.com/', 'https://www.breachlock.com/how-it-works/','http://testasp.vulnweb.com/showforum.asp?id=2','http://testasp.vulnweb.com/']


#usign regex
#get base url 
regex = re.compile(r'((http:\/\/|https:\/\/)?(www\.)?[\w.]*\.?com)', re.IGNORECASE)

base_urls = [] 

for url in urls:
    base_url = re.match(regex, url).group(1) + '/robots.txt'
    base_urls.append(base_url) 


for url in set(base_urls):
    try:
        r = requests.get(url)
        # get the content of the robots.txt file
        content = r.text
        print(f"\nThe robots.txt file content of {url} is \n {content}\n")
    except:
        print('\trobots.txt does not exist')

#alternate way 

origin_urls = list()
for url in urls:
    origin_url = furl(url).origin
    if origin_url not in origin_urls:
        origin_urls.append(origin_url)

for url in origin_urls:
    robot_url = f"{url}/robots.txt"
    print(robot_url)
    try:
        resp = requests.get(robot_url)
        content = resp.text
        print(f"\n The robots.txt file content of {url} is \n{content}\n")
    except:
        print(f"\t robots.txt does not exist for {url}")

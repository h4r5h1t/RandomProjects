import requests
import re 

urls = ['https://www.breachlock.com/', 'https://www.breachlock.com/how-it-works/','http://testasp.vulnweb.com/showforum.asp?id=2','http://testasp.vulnweb.com/']

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
#! python3

import bs4, requests, sys

def getAmazonPrice(productUrl):
    req = requests.get(pruductUrl)
    req.raise_for_status()

    soup = bs4.BeautifulSoup(req.text)
    elems = soup.select("# PUT CSS PATH OF THE PRICE HERE")
    return elems[0].text.strip()



prince = getAmazonPrice('sys.argv[1]')
print (f"The price is {price}")

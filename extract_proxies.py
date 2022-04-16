import requests
from bs4 import BeautifulSoup
import concurrent.futures 
import re

def getProxies():

	r = requests.get('https://free-proxy-list.net/')
	soup = BeautifulSoup(r.content,'html.parser')
	proxies=str(soup.find('textarea'))

	match = re.findall(r'[0-9]+(?:\.[0-9]+){3}:[0-9]+', proxies)
	return(match)


proxylist=getProxies()

def extract(proxy):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'}
    try:

        r = requests.get('https://httpbin.org/ip', headers=headers, proxies={'http//':proxy,'https//': proxy}, timeout=1)
        if r.status_code == 200:
        	print(proxy) 
    except requests.ConnectionError as err:
        pass

with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(extract,proxylist)

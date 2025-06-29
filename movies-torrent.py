import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,pt;q=0.8",
    "Connection": "keep-alive",
    "Referer": "https://1337x.to/home/",
    "Upgrade-Insecure-Requests": "1",
    "Cookie": "cf_clearance=32wMSLaWsDDOcDfGAhCPtTLiQ0F02hGRxAiINqBgols-1751224042-1.2.1.1-UWA83y2HooJjLMkff.qcy45WdXCffaUCPlhcsLHeOPzQsLhdv4n3fzTyg9NyOPcM4yzgqg8CiJ2.C394RWusnurmTs9V2lggVDFVvA5MXO8SNrFCH0gLq_lR956rc.gjWfEhexg0tlCxTA8XDL5VFuJPgwJm_Id0IHvokhAjr6XVYSVfhg6XZxx1a1v39uayFg1hVVOgwNxvn3JLrBRZ.Ejcpwc5Mh5HBm4DemHqHYEnbUATAI3pT_Lexw_8.97ttgJelvVLdVQ1X0DTJJG8Tj_wD1zAzg0rcaS2ECc23dcye4PgOrXIM4G8fqnUowJL1XH1Bd3Ndit9h8hSLdMjNiWvgb4kmmQiDspVa8z8ECGzcMMLNDt4fMmlk3osKD4V"  # completa se for necessário
}

pages = 1
link = f'https://1337x.to/search/dragon+ball+z/{pages}/'

response = requests.get(link,headers=headers)

if response.status_code == 200:
    print('STATUS: ',response.status_code,'- Request successful!')
    print('URL: ', response.url)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    cards = soup.find_all('tr', class_='odd')
    print(f'Found {len(cards)} torrents:')
    print('-----------------------------------')
    
    # for card in cards:
    #     print('-----------------------------------')
    #     name = job.find('h2', class_='h3 font-weight-bold text-body mb-8')
    #     name = str(name)
    #     print('Job Title:', name.replace('<h2 class="h3 font-weight-bold text-body mb-8">', '').strip().replace('</h2>',''))
else:
    print('Request failed with status code:', response.status_code)
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

response = requests.get(link, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', class_='table-list')
    if table:
        rows = table.find_all('tr')[1:]  # Ignora o cabeçalho
        for row in rows:
            title_col = row.find('td', class_='coll-1 name')
            if title_col:
                a_tag = title_col.find('a', href=True)
                if a_tag:
                    title = a_tag.text.strip()
                    torrent_link = 'https://1337x.to' + a_tag['href']
                    print(f'Title: {title}')
                    print(f'Link: {torrent_link}')
                    print('---')
else:
    print('Falha na requisição. Código:', response.status_code)
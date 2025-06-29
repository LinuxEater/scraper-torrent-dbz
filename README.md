# 1337x Torrent Scraper

Este é um script Python simples para fazer scraping dos títulos e links dos torrents na página de busca do site [1337x.to](https://1337x.to).

---

## Funcionalidades

- Busca torrents pelo termo "dragon ball z" (pode ser modificado no código).
- Extrai o título e o link para a página do torrent.
- Faz requisição HTTP com headers para simular navegador real.
- Usa BeautifulSoup para parsear o HTML.

---

## Requisitos

- Python 3.7+
- Bibliotecas Python:
  - requests
  - beautifulsoup4

---

## Como usar

1. Clone ou baixe este repositório.
2. Instale as dependências:
   ```bash
   pip install requests beautifulsoup4
   ```
3. Execute o script:
   ```bash
   python scraper.py
   ```
4. Veja a saída no terminal com os títulos e links dos torrents.

---

## Atenção

- O site 1337x pode usar proteção Cloudflare que bloqueia bots.  
- Para contornar isso, pode ser necessário usar um cookie válido `cf_clearance` ou ferramentas como `cloudscraper` ou `selenium`.
- Cookies expiram, então pode ser necessário atualizar periodicamente.

---

## Exemplo de resultado

```
Title: Dragon Ball Z Kai Episode 01 ...
Link: https://1337x.to/torrent/1234567/dragon-ball-z-kai-episode-01/
---
Title: Dragon Ball Z Movie 01 ...
Link: https://1337x.to/torrent/2345678/dragon-ball-z-movie-01/
---
```

---

## Personalização

- Modifique a variável `pages` para buscar em outras páginas.
- Modifique o termo na URL para buscar outros torrents.

---

## Contato

Para dúvidas, sugestões ou contribuições, entre em contato:  
**moisessouzasantos001@gmail.com**

---

## Licença

Este projeto está licenciado sob a licença MIT.

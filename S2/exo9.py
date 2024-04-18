# Exercice 9: Programmation asynchrone
# Créez un programme qui effectue des requêtes asynchrones à plusieurs URL en même temps, en utilisant les fonctionnalités asynchrones de Python.

import asyncio
import aiohttp

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def fetch_multiple_urls(urls):
    tasks = [fetch_url(url) for url in urls]
    return await asyncio.gather(*tasks)

# Exemple d'utilisation
urls = ['https://example.com', 'https://example.org', 'https://example.net']
results = asyncio.run(fetch_multiple_urls(urls))
print(results)

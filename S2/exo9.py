# Exercice 9: Programmation asynchrone
# Créez un programme qui effectue des requêtes asynchrones à plusieurs URL en même temps, en utilisant les fonctionnalités asynchrones de Python.

import asyncio
import aiohttp


urls = ['https://example.com', 'https://example.org', 'https://example.net']

async def fetch(url):

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:15], "...")


async def main(urls):
    tasks = []
    for url in urls:
        task = asyncio.create_task(fetch(url))
        tasks.append(task)
    await asyncio.gather(*tasks)


result = asyncio.run(main(urls))
print(result)

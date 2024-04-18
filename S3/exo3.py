# Exercice 3: Coroutines avancées
# Écrivez une coroutine qui simule un traitement asynchrone de données provenant de multiples sources et les agrège de manière efficace.

import asyncio

async def async_data_processing(data_source):
    # Simule un traitement asynchrone
    await asyncio.sleep(2)
    processed_data = data_source * 2
    return processed_data

async def aggregate_async_data(data_sources):
    tasks = [async_data_processing(source) for source in data_sources]
    return await asyncio.gather(*tasks)

# Exemple d'utilisation
data_sources = [1, 2, 3, 4]
results = asyncio.run(aggregate_async_data(data_sources))
print(results)

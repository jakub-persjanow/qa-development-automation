import asyncio
import aiohttp
import time

# SYNC
# def synchronous_chef():
#     print("Putting toast into toaster")
#     time.sleep(2)
#     print("Toast is ready")

#     print("Cooking egg")
#     time.sleep(2)
#     print("Egg is ready")

# start_time = time.time()
# synchronous_chef()
# end_time = time.time()

# print(f"It took {end_time-start_time} seconds")

#ASYNC
# async def make_toast():
#     print("Putting toast into toaster")
#     await asyncio.sleep(2)
#     print("Toast is ready")
#     return "Toast"

# async def make_egg():
#     print("Cooking egg")
#     await asyncio.sleep(3)
#     print("Egg is ready")
#     return "Egg"

# async def main():
#     start_time = time.time()

#     chef_tasks = await asyncio.gather(
#         make_toast(),
#         make_egg()
#     )

#     end_time = time.time()
#     print(f"It took {end_time-start_time} seconds")
#     print(f"Chef cooked: {chef_tasks}")

# asyncio.run(main())

# REAL WORLD EXAMPLE
async def fetch_status_async(session, url):
    print(f"Fetching {url}...")
    async with session.get(url) as response:
        print(f"Finished {url} with status {response.status}")
        return response.status
    
async def main_async():
    urls = [
        "https://www.python.org",
        "https://www.google.com",
        "https://www.github.com",
        # "https://www.dupppa.pl"
    ]
    start = time.time()
    async with aiohttp.ClientSession() as session:
        # Create a list of tasks to run
        # tasks = []
        # for url in urls:
        #     task = fetch_status_async(session, url)
        #     tasks.append(task)
        tasks = [fetch_status_async(session, url) for url in urls]
        # Wait for all tasks to complete
        await asyncio.gather(*tasks)

    end = time.time()
    print(f"\nAsync fetching took {end - start:.2f} seconds.")

asyncio.run(main_async())
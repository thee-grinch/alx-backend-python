import asyncio

async def fetch_data(url):
    # Simulate an asynchronous network request
    await asyncio.sleep(1)
    return f"Data from {url}"

async def main():
    urls = ["https://example.com", "https://google.com", "https://github.com"]

    # Fetch data from multiple URLs asynchronously using async comprehensions
    results = [await fetch_data(url) for url in urls]

    # Print the results
    for result in results:
        print(result)

# Run the main function
asyncio.run(main())
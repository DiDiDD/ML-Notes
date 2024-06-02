import asyncio

# coroutine: function / object
# task:

async def main():
    print('Hello')
    await asyncio.sleep(1)
    print('world')

asyncio.run(main())
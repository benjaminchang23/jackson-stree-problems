import asyncio

async def grond():
    print("grond")
    await asyncio.sleep(1)
    print("GROND")

asyncio.run(grond())
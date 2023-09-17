import asyncio
import time
import typing


task_list = []

async def grond(count: int):
    print("grond breakfast " + str(count))
    await asyncio.sleep(count)
    print("grond sleeps quietly " + str(count))

async def main():

    for i in range(10):
        print("grond awakens")
        task = asyncio.create_task(grond(count=i))

        # Add task to the set. This creates a strong reference.
        task_list.append(task)

        # To prevent keeping references to finished tasks forever,
        # make each task remove its own reference from the set after
        # completion:
        # task.add_done_callback(task_set.discard)

    print("grond makes a big breakfast")

    for i in range(10):
        await task_list[i]
        print("foo")

    print("dreams")

asyncio.run(main())


import asyncio
import typing


task_set = set()

async def grond(count: int):
    await asyncio.sleep(count)
    print("grond " + str(count))

async def main():

    for i in range(2):
        for i in range(10):
            task = asyncio.create_task(grond(count=i))

            # Add task to the set. This creates a strong reference.
            task_set.add(task)

            # To prevent keeping references to finished tasks forever,
            # make each task remove its own reference from the set after
            # completion:
            # task.add_done_callback(task_set.discard)
        
        for task in task_set:
            await task
        
        print("dreams")


asyncio.run(main())
import asyncio

async def first_function():
    await asyncio.sleep(2)
    print("hello world in function one")

async def second_function():
    await asyncio.sleep(2)
    print("hello world in function two")

async def third_function():
    await asyncio.sleep(2)
    print("hello world in third function")

async def multi_function():
    # create 3 tasks at once
    # task1 = asyncio.create_task(first_function())
    # task2 = asyncio.create_task(second_function())
    # task3 = asyncio.create_task(third_function())

    # wait for all tasks to finish
    # await task1
    # await task2
    # await task3
    
    #  Another way to do the task simultaneously
    await asyncio.gather(first_function(),second_function(),third_function())

asyncio.run(multi_function())

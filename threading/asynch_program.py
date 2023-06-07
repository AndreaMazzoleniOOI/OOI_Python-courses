import asyncio


async def stupid_main():   # this is a co-routin
    print('Andrea')
    await func('Doing') # need await to run a co-routine
    print('Finish')


async def task_main():
    """this is a co-routine. Finish is printed as soon as task starts without waiting for task to finish"""
    print('Andrea')
    task = asyncio.create_task(func('Doing'))
    print('Finish')


async def need_some_data_from_func():
    """this is a co-routine. Finish is printed as soon as task starts without waiting for task to finish"""
    print('Andrea')
    task = asyncio.create_task(func('Doing'))
    print('Finish')
    await asyncio.sleep(5)  # this simulates some stuff we can do while waiting for task
    value = await task # wait task to be completed
    print(f'task returned {value}')


async def func(text):
    print(text)
    await asyncio.sleep(10)  # we need await to run the co-routine func
    return 1

# asyncio.run(stupid_main())  # start the co-routine, this print finish AFTER executing func (so it has to wait for 10s).
asyncio.run(task_main())  # start the co-routine, this print finish as soon as func is called without waiting for it to be completed.
asyncio.run(need_some_data_from_func())




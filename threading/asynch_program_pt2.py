import asyncio
import time

async def fetch_data():
    print('Fetching...')
    await asyncio.sleep(2)
    print('Done')
    return {'data': 1}


async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)
    return i

async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())

    value = await task1 # wait for task1 to finish befor printing is value
    print(value)
    i = await task2  # if we do not add this part task2 will not be done executing and the process is killed
    print(f'Sum is {value["data"]}+{i} = {value["data"]+i}')


def sync_main():
    print('Fetching...')
    time.sleep(2)
    print('Done')
    value = {'data': 1}
    for i in range(10):
        print(i)
        time.sleep(0.25)
    print(f'Sum is {value["data"]}+{i} = {value["data"]+i}')

start = time.time()
asyncio.run(main())
print(f'Async took {time.time()-start}')
print('\n\n\n')
# for comparison
start = time.time()
sync_main()
print(f'Sync took {time.time()-start}')


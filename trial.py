import asyncio


async def count(number, count):
    print('finding the number {} numbers after {}'.format(count, number))
    for i in range(count):  # just to make task longer, to verify asynchronous processing
        i += 1
        await asyncio.sleep(1)
    number += count
    print("the number after adding {} is {}".format(count, number))
    return number


async def main():
    task1 = loop.create_task(count(1, 10))
    task2 = loop.create_task(count(5, 20))
    task3 = loop.create_task(count(7, 30))
    await asyncio.wait([task1, task2, task3])

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()

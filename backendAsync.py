import asyncio
import os
import random  # only for testing purposes
import time
from opcua import Client, ua
# import station_connect_class as _
machstate_1 = 'Ready'
machstate_2 = 'Ready'
machstate_3 = 'Ready'


async def taskOne():
    # if not _.LightCurtain1.get_value():
    global machstate_1
    # replace this if condition with the lightcurtain variable while testing for machines
    if random.choice([True, False]):
        # os.system('mpg123 curtain_breach_message_hindi.mp3')  #uncomment this when audio files available in same folder
        machstate_1 = 'Error'
        print('machine 1 curtain breached')


async def taskTwo():
    # if _.LightCurtain2.get_value():
    global machstate_2
    if random.choice([True, False]):
        # os.system('mpg123 curtain_breach_message_hindi.mp3')
        machstate_2 = 'Error'
        print('machine 2 curtain breached')


async def taskThree():
    # if _.LightCurtain3.get_value():
    global machstate_3
    if random.choice([True, False]):
        # os.system('mpg123 curtain_breach_message_hindi.mp3')
        machstate_3 = 'Error'
        print('machine 3 curtain breached')


async def main():
    task1 = loop.create_task(taskOne())
    task2 = loop.create_task(taskTwo())
    task3 = loop.create_task(taskThree())
    await asyncio.wait([task1, task2, task3])

if __name__ == '__main__':
    # _.connectMachineOne()
    # _.connectMachineTwo()
    # _.connectMachineThree()
    print('connected to machines')
    # _.client1.disconnect()
    # _.client2.disconnect()
    # _.client3.disconnect()
    loop = asyncio.get_event_loop()

    while True:
        # _.client1.connect()
        # _.client2.connect()
        # _.client3.connect()
        loop.run_until_complete(main())
        print('checked once')
        time.sleep(5)
        # _.client1.disconnect()
        # _.client2.disconnect()
        # _.client3.disconnect()
    loop.close()

""" Упражнение 1
Описание задачи:
Расставьте ключевое слово await, там где это необходимо, чтобы код заработал;
При запуске кода на stepik, укажите версию python 3.10+
import asyncio

async def task1():
    asyncio.sleep(1)
    print("Привет из корутины task1")

async def task2():
    asyncio.sleep(1)
    print("Привет из корутины task2")

async def main():
    asyncio.create_task(task1())
    asyncio.create_task(task2())

asyncio.run(main())
Sample Input:
Sample Output:
    Привет из корутины task1
    Привет из корутины task2
"""
import asyncio

async def task1():
    await asyncio.sleep(1)
    print("Привет из корутины task1")

async def task2():
    await asyncio.sleep(1)
    print("Привет из корутины task2")

async def main():
    await asyncio.create_task(task1())
    await asyncio.create_task(task2())

asyncio.run(main())

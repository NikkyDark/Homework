import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    for ball_number in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял шар {ball_number}')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    tasks = [
        start_strongman('Иван', 3),
        start_strongman("Петр", 4),
        start_strongman("Александр", 5)
    ]
    for tasks in tasks:
        await tasks

if __name__ == '__main__':
    asyncio.run(start_tournament())
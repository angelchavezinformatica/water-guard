import uasyncio as asyncio

from app import routes
from schedule import schedule, TaskType
from server import Server
from state import state


async def server_task():
    server = Server(routes)
    await server.run_non_blocking()


async def schedule_task():
    while True:
        next_time = schedule.get_next_time()

        if next_time is None:
            await asyncio.sleep(5)
            continue

        await asyncio.sleep(next_time)

        task = schedule.get_next_task()

        if task.type == TaskType.ON:
            state.bomb.on()
        elif task.type == TaskType.OFF:
            state.bomb.off()

        schedule.delete_first_task()


async def main():
    asyncio.create_task(schedule_task())
    asyncio.create_task(server_task())

    while True:
        await asyncio.sleep(3600)

asyncio.run(main())

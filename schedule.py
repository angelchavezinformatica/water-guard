import time


class TaskType:
    ON = 'ON'
    OFF = 'OFF'


class Task:
    def __init__(self, type: str, time: float) -> None:
        self.type = type
        self.time = time

    def __repr__(self) -> str:
        return f"<Task type={self.type} time={self.time}>"


class Schedule:

    def __init__(self, initial_schedule: list[Task] = []) -> None:
        self.schedule = initial_schedule

    def add_task(self, task: Task):
        self.schedule.append(task)
        self.schedule.sort(key=lambda t: t.time)

    def get_next_time(self):
        try:
            return self.schedule[0].time - time.time()
        except IndexError:
            return

    def get_next_task(self):
        try:
            return self.schedule[0]
        except IndexError:
            return

    def delete_first_task(self):
        self.schedule.pop(0)


schedule = Schedule([
    Task(TaskType.ON, time.time() + 5),
    Task(TaskType.OFF, time.time() + 8),
    Task(TaskType.ON, time.time() + 10),
    Task(TaskType.OFF, time.time() + 15),
    Task(TaskType.ON, time.time() + 25),
    Task(TaskType.OFF, time.time() + 30),
])

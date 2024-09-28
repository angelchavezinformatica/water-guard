from machine import Pin


class PinState:
    def __init__(self, pin: int, mode: any) -> None:
        self.pin = Pin(pin, mode)
        self.state = 0

    def on(self):
        self.pin.on()
        self.state = 1

    def off(self):
        self.pin.off()
        self.state = 0

    def get_state(self):
        return self.state


class State:

    def __init__(self) -> None:
        self.bomb = PinState(5, Pin.OUT)


state = State()

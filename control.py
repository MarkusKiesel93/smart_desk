from gpio import Gpio
from config import config


class Control():
    def __init__(self):
        self.gpio = Gpio()

    def up(self):
        self.gpio.on(config.pin_power_left)


if __name__ == '__main__':
    control = Control()
    control.up()
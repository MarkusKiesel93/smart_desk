import RPi.GPIO as GPIO
from time import sleep

from config import config

# todo: change exceptions to logging

test_time = 10

class Control():
    def __init__(self):
        GPIO.setwarnings(False)
        self.waiting_time: int = 1

    def test(self):
        self._pin_on(config.pin_power_supply)
        sleep(60)
        self._pin_off(config.pin_power_supply)


    def up(self):
        self._pin_on(config.pin_power_supply)
        sleep(self.waiting_time)
        for pin in config.pins_polarity_left:
            self._pin_on(pin)
        for pin in config.pins_polarity_right:
            self._pin_on(pin)
        sleep(self.waiting_time)
        self._power_on()
        sleep(test_time)
        self._power_off()
        for pin in config.pins_polarity_left:
            self._pin_off(pin)
        for pin in config.pins_polarity_right:
            self._pin_off(pin)
        self._teardown()

    def down(self):
        self._pin_on(config.pin_power_supply)
        sleep(self.waiting_time)
        self._power_on()
        sleep(test_time)
        self._power_off()
        self._teardown()

    def _power_on(self):
        # self._pin_on(config.pin_power_supply)
        self._pin_on(config.pin_power_left)
        self._pin_on(config.pin_power_right)

    def _power_off(self):
        self._pin_off(config.pin_power_left)
        self._pin_off(config.pin_power_right)
        # self._pin_off(config.pin_power_supply)

    def _pin_on(self, pin):
        try:
            GPIO.setmode(config.gpio_mode)
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)
        except Exception as ex:
            print(f'Exception durnig turning on pin: {pin}')
            print(ex)

    def _pin_off(self, pin):
        try:
            GPIO.setmode(config.gpio_mode)
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.HIGH)
        except Exception as ex:
            print(f'Exception durnig turning off pin: {pin}')
            print(ex)

    def _teardown(self):
        GPIO.cleanup()



if __name__ == '__main__':
    control = Control()
    # control.test()
    control.up()
    sleep(1)
    #control.down()
import RPi.GPIO as GPIO
from time import sleep

from config import config

# todo: change exceptions to logging


class Control():
    def __init__(self):
        GPIO.setwarnings(False)
        self.waiting_time: int = 1

    def up(self):
        for pin in config.pins_polarity_left:
            self._pin_on(pin)
        for pin in config.pins_polarity_right:
            self._pin_on(pin)
        sleep(self.waiting_time)
        self._power_on()

    def down(self):
        self._pin_on(config.pin_power_supply)
        sleep(self.waiting_time)
        self._power_on()
    
    def stop(self):
        self._power_off()
        for pin in config.pins_polarity_left:
            self._pin_off(pin)
        for pin in config.pins_polarity_right:
            self._pin_off(pin)
        self._teardown()

    def _power_on(self):
        self._pin_on(config.pin_power_supply)
        sleep(self.waiting_time)
        self._pin_on(config.pin_power_left)
        self._pin_on(config.pin_power_right)

    def _power_off(self):     
        self._pin_off(config.pin_power_left)
        self._pin_off(config.pin_power_right)
        sleep(self.waiting_time)
        self._pin_off(config.pin_power_supply)

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
    control._pin_on(config.pin_power_supply)
    control._pin_on(config.pin_power_right)
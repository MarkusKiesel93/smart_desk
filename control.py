import RPi.GPIO as GPIO
from time import sleep

from config import config


class Control():
    def __init__(self):
        GPIO.setmode(config.gpio_mode)
        GPIO.setwarnings(False)

    def test(self):
        try:
            GPIO.setup(config.pin_power_left, GPIO.OUT)
            for pin in config.pin_polarity_left:
                GPIO.setup(pin, GPIO.OUT)
            GPIO.output(config.pin_power_left, GPIO.LOW)
            sleep(3)
            GPIO.output(config.pin_power_left, GPIO.HIGH)
            sleep(1)
            for pin in config.pin_polarity_left:
                GPIO.output(pin, GPIO.LOW)
            sleep(1)
            GPIO.output(config.pin_power_left, GPIO.LOW)
            sleep(3)
            GPIO.output(config.pin_power_left, GPIO.HIGH)
            for pin in config.pin_polarity_left:
                GPIO.output(pin, GPIO.HIGH)
        except Exception as ex:
            print(ex)
        finally:
            self.teardown()
            
    def teardown(self):
        GPIO.cleanup()



if __name__ == '__main__':
    control = Control()
    control.test()
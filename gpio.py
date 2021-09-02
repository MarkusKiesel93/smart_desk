import RPi.GPIO as GPIO

from config import config


class Gpio:
    def __init__(self):
        GPIO.setmode(config.gpio_mode)

    def on(self, pin: int):
        try:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.HIGH)
        except Exception as ex:
            print("turn on failed!")
            print(ex)

    def off(self, pin: int):
        try:
            GPIO.setwarnings(False)
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)
        except Exception as ex:
            print("turn off failed!")
            print(ex)
        finally:
            GPIO.cleanup()

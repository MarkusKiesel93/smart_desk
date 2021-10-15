import RPi.GPIO as GPIO
import time

from config import config

GPIO.setmode(GPIO.BCM)

def setup(pin_trig, pin_echo):
    GPIO.setup(pin_trig, GPIO.OUT)
    GPIO.output(pin_trig, 0)
    GPIO.setup(pin_echo, GPIO.IN)


def measure(pin_trig, pin_echo):
    GPIO.output(pin_trig, 1)
    time.sleep(1)
    GPIO.output(pin_trig, 0)

    while GPIO.input(pin_echo) == 0:
        pass
    start = time.time()

    while GPIO.input(pin_echo) == 1:
        pass
    stop = time.time()

    return int((stop - start) * 170 * 100 * 10)


if __name__ == '__main__':
    setup(config.pin_sensor_trig_left, config.pin_sensor_echo_left)
    setup(config.pin_sensor_trig_right, config.pin_sensor_echo_right)
    time.sleep(0.1)
    distance_left = measure(config.pin_sensor_trig_left, config.pin_sensor_echo_left)
    distance_right = measure(config.pin_sensor_trig_right, config.pin_sensor_echo_right)
    print('LEFT \t RIGHT')
    print(f'{distance_left}\t{distance_right}')

    GPIO.cleanup()

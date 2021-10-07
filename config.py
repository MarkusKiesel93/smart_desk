from pydantic import BaseSettings
import RPi.GPIO as GPIO


class Config(BaseSettings):
    cors_allowed_origins = ['*']
    cors_allowed_methods = ['GET', 'POST']
    cors_allowed_headers = ['*']

    gpio_mode = GPIO.BCM
    pin_power_supply: int = 21
    pin_power_left: int = 6
    pin_power_right: int = 5
    pins_polarity_left: List[int] = [16, 20]
    pins_polarity_right: List[int] = [13, 19]


config = Config()

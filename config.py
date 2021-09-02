from pydantic import BaseSettings
import RPi.GPIO as GPIO


class Config(BaseSettings):
    cors_allowed_origins = ['*']
    cors_allowed_methods = ['GET', 'POST']
    cors_allowed_headers = ['*']

    gpio_mode = GPIO.BCM
    pin_power_left = 5
    pin_power_right = 6
    pin_polarity_pos_left = 13
    pin_polarity_neg_left = 19
    pin_polarity_pos_right = 16
    pin_polarity_neg_right = 20


config = Config()

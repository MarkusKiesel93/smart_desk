from curtsies import Input
from control import Control
from config import config
from time import sleep

control = Control()

try:
    with Input() as input_generator:
        for e in input_generator:
            if e == '<UP>':
                print('UP')
                control.up()
            if e == '<DOWN>':
                print('DOWN')
                control.down()
            if e == '<SPACE>':
                print('STOP')
                control.stop()
            if e == '<ESC>':
                print('CANCEL')
                control.stop()
                break
            if e == 'w':
                print('LEFT UP')
                for pin in config.pins_polarity_left:
                    control._pin_on(pin)
                sleep(control.waiting_time)
                control._pin_on(config.pin_power_supply)
                sleep(control.waiting_time)
                control._pin_on(config.pin_power_left)
            if e == 's':
                print('LEFT DOWN')
                control._pin_on(config.pin_power_supply)
                sleep(control.waiting_time)
                control._pin_on(config.pin_power_left)
            if e == 'e':
                print('RIGHT UP')
                for pin in config.pins_polarity_right:
                    control._pin_on(pin)
                sleep(control.waiting_time)
                control._pin_on(config.pin_power_supply)
                sleep(control.waiting_time)
                control._pin_on(config.pin_power_right)
            if e == 'd':
                print('RIGHT DOWN')
                control._pin_on(config.pin_power_supply)
                sleep(control.waiting_time)
                control._pin_on(config.pin_power_right)
except KeyboardInterrupt:
    print('\nExit with "Ctrl+c"')

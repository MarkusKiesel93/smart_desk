from curtsies import Input
from control import Control

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
except KeyboardInterrupt:
    print('\nExit with "Ctrl+c"')

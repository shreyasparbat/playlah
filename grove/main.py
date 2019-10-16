# Imports
import time
from datetime import datetime
import grovepi

def get_input():
    if grovepi.digitalRead(2) == 1:
        return [2, datetime.now()]
    if grovepi.digitalRead(3) == 1:
        return [3, datetime.now()]
    if grovepi.digitalRead(4) == 1:
        return [4, datetime.now()]
    if grovepi.digitalRead(5) == 1:
        return [5, datetime.now()]
    if grovepi.digitalRead(6) == 1:
        return [6, datetime.now()]
    if grovepi.digitalRead(7) == 1:
        return 'end'

def end_game(inputs):
    print('game over')

# Run script if main process
if __name__ == '__main__':
    # Set relevant digital ports to input
    for i in range(2, 8):
        grovepi.pinMode(i, 'INPUT')
    
    # Store inputs
    inputs = [[0,0]]
    
    # Start inifite loop
    while True:
        try:
            # Receive and store unique inputs
            input_ = get_input()

            # If 'end', then end the game
            if input_ == 'end':
                end_game(inputs)
                exit(0)

            # Else store them
            if input_ and input_[0] != inputs[-1][0]:
                inputs.append(input_)
                print('Key:', input_[0], 'Timestamp:', str(input_[1]), sep=' ')
            
            # Sleep
            time.sleep(0.01)
        except IOError as e:
            print(e)

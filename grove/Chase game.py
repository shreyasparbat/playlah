# Imports
import time
from datetime import datetime
import requests
import grovepi
import random

# Default client name
clientname = 'test'

# Format mech key input
def get_input():
    if grovepi.digitalRead(2) == 1:
        return { 'clientname': clientname, 'tappedkey': 2, 'timestamp': str(datetime.now())}
    if grovepi.digitalRead(3) == 1:
        return { 'clientname': clientname, 'tappedkey': 3, 'timestamp': str(datetime.now())}
    if grovepi.digitalRead(4) == 1:
        return { 'clientname': clientname, 'tappedkey': 4, 'timestamp': str(datetime.now())}
    if grovepi.digitalRead(5) == 1:
        return { 'clientname': clientname, 'tappedkey': 5, 'timestamp': str(datetime.now())}
    if grovepi.digitalRead(6) == 1:
        return { 'clientname': clientname, 'tappedkey': 6, 'timestamp': str(datetime.now())}
    if grovepi.digitalRead(7) == 1:
        return 'end'


# Send results to server and exit
def end_game(scores):
    # requests.post('<url>', json={'scores': scores}) <Send scores to server> 
    print(scores)


# Run script if main process
if __name__ == '__main__':
    # Set relevant digital ports to input
    for i in range(2, 8):
        grovepi.pinMode(i, 'INPUT')
    
    # Store scores
    scores = []

    # To ensure that the random number generated in not the same as last time
    prev_randint = 0
    
    # Start inifite loop
    while True:
        try:
            # Create a random number
            to_press = random.randint(2,6)
            while to_press == prev_randint:
                to_press = prev_randint
            prev_randint = to_press

            # Light up key
            print(to_press) # <Change to lighting this key>

            # Append the random button to scores with timestamp
            scores.append({'clientname': clientname, 'randomkey': to_press, 'timestamp': str(datetime.now())})

            # Start another loop which only ends with correct key press
            while True:
                # Receive and store unique inputs
                input_ = get_input()

                # If 'end', then end the game
                if input_ == 'end':
                    end_game(scores)
                    exit(0)
                elif input_ and input_['tappedkey'] == to_press:
                    scores.append(input_)
                    print('Correct!')
                    break
            
            # Sleep
            time.sleep(0.01)
        except IOError as e:
            print(e)

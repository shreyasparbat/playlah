# Imports
import time
from datetime import datetime
import requests
import grovepi

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
    # POST scores to server
    
    requests.post('http://ec2-54-169-209-209.ap-southeast-1.compute.amazonaws.com:3000/scores/add-demo-scores', json={
        'scores': scores
    })
    print('game over')


# Run script if main process
if __name__ == '__main__':
    # Set relevant digital ports to input
    for i in range(2, 8):
        grovepi.pinMode(i, 'INPUT')
    
    # Store scores (first entry is junk)
    scores = [{ 'clientname': clientname, 'tappedkey': 0, 'timestamp': '2019-09-09'}]
    
    # Start inifite loop
    while True:
        try:
            # Receive and store unique inputs
            input_ = get_input()

            # If 'end', then end the game
            if input_ == 'end':
                end_game(scores[1:])
                exit(0)

            # Else store them
            if input_ and input_['tappedkey'] != scores[-1]['tappedkey']:
                scores.append(input_)
                print('Key: ' + str(input_['tappedkey']) + ', Timestamp: ' + input_['timestamp'])
            
            # Sleep
            time.sleep(0.01)
        except IOError as e:
            print(e)

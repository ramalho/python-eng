from time import strftime, sleep


while True:
    now = strftime('%H:%M:%S')
    print(now, end='', flush=True)
    sleep(.1)    
    print('\r' * len(now), end='', flush=True)

from time import sleep
from datetime import datetime


while True:
    now = datetime.now().strftime('%H:%M:%S.%f')[:10]
    try:
        print(now, end='', flush=True)
        sleep(.1)
    except KeyboardInterrupt:
        break    
    finally:
        print('\r' * len(now), end='', flush=True)

import webbrowser
import os
from datetime import datetime
from pytz import timezone
import time


def isFriday():
    today = datetime.now()
    inCali = today.astimezone(timezone('US/Pacific'))
    if inCali.weekday() == 4:
        return True
    else:
        return False

def shoot():
    # HTML file path
    html_file_path = os.path.abspath("TIFIC.html")

    # Opens HTML file in firefox
    webbrowser.get('firefox').open(f"file://{html_file_path}")
    exit()



def time_keeper():
    while True:
        if isFriday() == True:
            shoot()
        else:
            time.sleep(60)

if __name__ == "__main__":
    time_keeper()
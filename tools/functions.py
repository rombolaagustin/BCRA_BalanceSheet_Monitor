
import os
import time
from urllib import request
from datetime import datetime

# DOWNLOAD FILE
def download_file(url: str, filename: str, hours: float):
    try: 
        creation_date = os.path.getctime(filename)
        now = datetime.now().timestamp()
        if hours*60*60 < now-creation_date:
            print(f'Downloading {filename} ...')
            response = request.urlretrieve(url, filename)
        else:
            print('OK: File is up to date')
    except:
        print(f'{filename} does not exist. Downloading...')
        response = request.urlretrieve(url, filename)

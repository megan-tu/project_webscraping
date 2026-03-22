import requests
r = requests.get('http://kcna.kp')
try:
    r = requests.get('http://175.45.176.10', timeout=5)
except requests.exceptions.ConnectTimeout:
    print('r.status_code=', r.status_code)
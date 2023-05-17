import requests
import sys
try:
    cla=float(sys.argv[1])
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    price=r.json()['bpi']["USD"]["rate_float"]
except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")
except requests.RequestException:
    pass
else:
    print(f"${(cla*price):,}")
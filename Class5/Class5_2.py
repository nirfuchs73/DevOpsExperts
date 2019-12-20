import urllib.request
import json

print('Welcome to currency converter')
try:
    amount = int(input('Please enter an amount of Shekeles to convert:'))
except ValueError as err:
    print(err)
    exit(1)

# Opening a web request
url = urllib.request.urlopen(
    "https://free.currconv.com/api/v7/convert?q=ILS_USD&compact=n&apiKey=a4d4d3d06c1404ad48a7")


# Decoding response to str
data = json.loads(url.read().decode())  # Decoding a web request
# Parsing results
results = data['results']
USD_ILS = results['ILS_USD']
val = USD_ILS['val']
print("{0:.2f}".format(int(amount) * val), 'USD')
print('Thanks for using our currency converter')

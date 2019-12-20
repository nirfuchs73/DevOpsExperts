import urllib.request
import json

# val = urllib.request.urlopen("https://www.google.com").read()
# print(val)


# x = '{ "name":"John", "age":30, "city":"New York"}'
# y = json.loads(x)
# print(y["age"])


# Opening a web request
url = urllib.request.urlopen(
    "https://free.currconv.com/api/v7/convert?q=USD_ILS&compact=n&apiKey=a4d4d3d06c1404ad48a7")
# Decoding response to str
data = json.loads(url.read().decode())  # Decoding a web request
# print(data)
# Parsing results
results = data['results']
USD_ILS = results['USD_ILS']
val = USD_ILS['val']
print(val)

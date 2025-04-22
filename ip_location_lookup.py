import requests
import json

ip = input("ip: ")
apiKey = 'aea9a520df037f69aceb74dc49bc77f9'
url = f'https://iplocate.io/api/lookup/{ip}?apikey={apiKey}'

response = requests.get(url)
data = response.json()

# Mooi formatteren en afdrukken
print(json.dumps(data, indent=4))

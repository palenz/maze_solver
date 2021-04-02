import requests
import json

id = '94a4dd75-8f32-4b64-ae9a-b27beb753e4a'
print_url = 'https://ponychallenge.trustpilot.com/pony-challenge/maze/a667a4a0-ea9f-4474-b814-82bc9777cc60/print'


response = requests.get(print_url)
res = response.text

print(res)
import random
import requests

def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

r = requests.post("https://api.deepai.org/api/text-generator", data ={'text':random_line('questions.txt')}, headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'})
body = r.json()
print(body['output'])

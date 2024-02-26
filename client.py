import requests
import random

for _ in range(1000):
	r = random.randint(10, 15)
	req = requests.get(f"http://127.0.0.1:81/{r}")
	print(req.text)

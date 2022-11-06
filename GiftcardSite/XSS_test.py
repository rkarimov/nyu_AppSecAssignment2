import requests
URL = 'http://127.0.0.1:8000/gift/?director=<script>alert("XSS exploited, muhahaha!")</script>'
init_session = requests.Session()
body = init_session.post(URL)

if body.text.find(""):
	print("XSS exploited")
else:
	print("XSS is fixed!")

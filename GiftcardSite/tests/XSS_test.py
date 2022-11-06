import requests
URL = 'https://google.com'
init_session = requests.Session()
body = init_session.post(URL)

if body.text.find(""):
	print("XSS exploited")
else:
	print("XSS is fixed!")

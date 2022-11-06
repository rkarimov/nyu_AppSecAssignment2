import requests
URL = 'https://google.com' ## hold URL, please change to url referenced in report to run test 
init_session = requests.Session()
body = init_session.post(URL)

if body.text.find(""):
	print("XSS exploited")
else:
	print("XSS is fixed!")

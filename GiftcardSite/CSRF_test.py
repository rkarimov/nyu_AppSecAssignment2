import requests

init_session = requests.Session()
cookies = requests.cookies.RequestsCookieJar()
target_url = 'http://127.0.0.1:8000/gift/0'
data  = {'uname':'threat_actor','pword':'admin'}
request_body = init_session.post(target_url, data=data, cookies=cookies)
body_text = init_session.get(target_url,cookies=cookies)
try:
	text.find("threat_actor")
	print("CSRF exploitable")
except: 
	print("CSRF is fixed!")
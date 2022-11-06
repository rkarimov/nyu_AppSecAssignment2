import requests

init_session = requests.Session()
cookies = requests.cookies.RequestsCookieJar()
target_url = 'https://google.com' ## hold URL, please change to url referenced in report to run test 

data  = {'uname':'threat_actor','pword':'admin'}
request_body = init_session.post(target_url, data=data, cookies=cookies)
body_text = init_session.get(target_url,cookies=cookies)
try:
	text.find("threat_actor")
	print("CSRF exploitable")
except: 
	print("CSRF is fixed!")

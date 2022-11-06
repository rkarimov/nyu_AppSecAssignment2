import requests

file = open('GiftcardSite/SQLInjectionAttack.gftcrd')
inflitration = 'https://google.com' ### hold URL, please change to url referenced in report to run test
init_session = requests.Session()
body = init_session.post(inflitration, data=file)
card_key = ""
if body.text.find(card_key):
	print("SQL Injection worked!")
else:
	print("Not exploitable to SQL Injection")

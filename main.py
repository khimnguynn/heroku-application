from requests import Session

ses = Session()

res = ses.get("https://api.ipify.org?format=json").json()
print(res["ip"])
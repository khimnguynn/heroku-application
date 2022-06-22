# from requests import Session
# import re
#
#
# def Get_Params():
#     ses = Session()
#     ses.headers.update({
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
#     })
#     res = ses.get("https://login.live.com/login.srf?").text
#     urlres = re.findall("(GetCredentialType[^']+)", res)
#     uaid = re.findall("&uaid=([^\"]+)", res)
#     client = re.findall("client_id=([^&]+)", res)
#     token = re.findall('" value="([^"]+)', res)
#     return urlres[0], uaid[0], client[0], token[0]
#
#
# def Check(email):
#     all = Get_Params()
#     ses = Session()
#     ses.headers.update({
#         "Accept": "application/json",
#         "Accept-Encoding": "gzip, deflate, br",
#         "client-request-id": "e37ffdec11c0245cb2e0",
#         "Content-Length": "641",
#         "Content-type": "application/json; charset=UTF-8",
#         "Host": "login.live.com",
#         "hpgact": "0",
#         "hpgid": "33",
#         "Origin": "https://login.live.com",
#         "Referer": "https://login.live.com/login.srf?",
#         "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
#         "sec-ch-ua-mobile": "?0",
#         "sec-ch-ua-platform": '"Windows"',
#         "Sec-Fetch-Dest": "empty",
#         "Sec-Fetch-Mode": "cors",
#         "Sec-Fetch-Site": "same-origin",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
#     })
#     url = "https://login.live.com/" + all[0]
#     data = {"username":f"{email}","uaid":"27451c7d66d1414d883da4f6c397da72","isOtherIdpSupported":"false","checkPhones":"false","isRemoteNGCSupported":"true","isCookieBannerShown":"false","isFidoSupported":"true","forceotclogin":"false","otclogindisallowed":"false","isExternalFederationDisallowed":"false","isRemoteConnectSupported":"false","federationFlags":3,"isSignup":"false","flowToken":"DYP3miIfkFn3QUAiQ3ROkBGvn5XJIfJqyCGePhpyfd3CQ6HH2b62VEyPzyjvDxPaPyEvBRxWjZl8bRJuuDaeXj*m30bjIR7W9w4!Lc332JHwlU53iwJU6XJpl3l*kECAsUtjkNiYbaBGt5tCpiNhC0XYI3JSgcZRdvoixy7OjX*41KEtxkYAsDkC1x*rTUSaL1ZsGohBo7*m1DpsfC8xeP9bZSmuKpqdf3xCLRuuSC2ovOcUobO4SpFkGih6Z*xtjw$$"}
#     res = ses.get("https://login.live.com/GetCredentialType.srf?opid=D968A409BCE6B6E6&id=38936&mkt=EN-US&lc=1033&uaid=27451c7d66d1414d883da4f6c397da72", json=data).json()
#     print(res)
#
#
# Check("hotmail@hotmail.com")

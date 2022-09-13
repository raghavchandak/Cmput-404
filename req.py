import requests

print(requests.__version__)

print(requests.get("https://raw.githubusercontent.com/raghavchandak/Cmput-404/main/req.py").text)

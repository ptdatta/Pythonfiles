import requests
# r = requests.get("https://financialmodelingprep.com/api/company/price/AAPL")
r = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=3c2542cd79e346a2a671014fcf2460f4")
print(r.text)
# print(r.status_code)

# url = "www.something.com"
# data = {
#     "p1":4,
#     "p2":8
# }
# r2 = requests.post(url=url, data=data)



# site-->https://codewithharry.com/videos/python-tutorials-for-absolute-beginners-81/
import requests

url = "http://www.weather.go.kr/share/js/marine_zone_info.js"
response = requests.get(url)
data = response.text
print(data)
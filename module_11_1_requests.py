from requests import get


response = get("https://static-maps.yandex.ru/1.x/?"
             "ll=49.102952,55.788698&"
             "spn=0.016457,0.00619&"
             "l=map")
with open("map.png", "wb") as file:
    file.write(response.content)

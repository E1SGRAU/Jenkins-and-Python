from lib.currency import get_currency

# Публічні дані по валютам:
# -> https://api.privatbank.ua/#p24/exchange <- 
# з посилання можна отримати URL
URL = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"

#Підключаємо функцію
get_currency(URL)

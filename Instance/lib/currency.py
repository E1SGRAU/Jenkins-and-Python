import requests

if __name__ == "__main__":
    pass
  
#Створимо функцію, яка отримує значення з посилання
def get_currency(URL):
  
  #Змінна відповіді:
  #вся інформація про наш запит тепер зберігається в об'єкті Response, що називається змінною responce
    responce = requests.get(URL)
  
  #Змінна валют:
  #responce.json() вказує об'єкту класу response формат json, у якому хочемо отримати дані
    currencies = responce.json()
  
  #Отримаємо дані, де: 
  # -> "ccy":"EUR" <- змінна яка відповідає за назву валюти
  # -> "base_ccy":"UAH" <- змінна яка відповідає за назву валюти в яку переведемо за відповідним курсом
  # -> "buy":"39.90000" <- відповідна ціна змінної EUR
  # -> "sale":"40.90000" <- відповідна ціна-відповідь змінної UAH
    for currency in currencies:
        print(currency['ccy'], " ", currency['base_ccy'],
              " | ", currency['buy'], " ", currency['sale'])
      
  #Наступний for відповідає за оформлення, який записуємо в файл під назвою currency.txt
    file = open('currency.txt', 'w')
    for item in currencies:
        file.write(item["ccy"] + " " + item["base_ccy"] + " " +
                   item["buy"] + " | " + item["sale"]+"\n")
    file.close
  #Отримаємо дані: 
  # -> USD UAH 38.90000 | 39.40000
  # -> EUR UAH 38.00000 | 39.00000
  # -> BTC USD 19660.1324 | 21729.6200
    print("Saved in file ", file)

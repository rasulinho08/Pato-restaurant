# import requests
# from bs4 import BeautifulSoup

# # Указываем URL сайта
# url = "https://preview.colorlib.com/theme/clyde/"

# # Отправляем запрос к сайту
# response = requests.get(url)

# # Проверяем, успешно ли мы получили страницу
# if response.status_code == 200:
#     # Разбираем HTML страницы с помощью BeautifulSoup
#     soup = BeautifulSoup(response.text, "html.parser")
    
#     # Находим все заголовки на странице (например, теги <h2>)
#     headings = soup.find_all("h2")
    
#     for heading in headings:
#         print(heading.text)  # Выводим текст заголовков

# else:
#     print("Ошибка при запросе:", response.status_code)
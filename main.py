from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import csv

# Adres sterownika
chrome_driver_path = "C:\development\chromedriver.exe"

# Nie wyłączanie okna po zakończeniu skryptu
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Wczytanie sterownika
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Adres strony z której będą zczytywane dane
driver.get("https://sofifa.com/players")

sleep(2)

# Zlokalizowanie kolumny overall rating i jej kilknięcie
overall_rating = driver.find_element(By.CSS_SELECTOR, 'th.col-oa[aria-label="Overall rating"]')
overall_rating.click()

# Utworzenie listy nazwisk
players_surname = driver.find_elements(By.CSS_SELECTOR, 'td.col-name > a[role="tooltip"] > div.ellipsis')

players_surname_text = []
for surname in players_surname[:15]:
    players_surname_text.append(surname.text)

# Utworzenie listy rating
players_rating = driver.find_elements(By.CSS_SELECTOR, 'td.col-oa[data-col="oa"]')

players_rating_text = []
for rating in players_rating[:15]:
    players_rating_text.append(rating.text)

# Połącz nazwiska z oceną
players_text = []
for i in range(len(players_surname_text)):
    players_text.append(players_surname_text[i] + " - " + players_rating_text[i])

# Zapisz nazwiska zawodników do pliku CSV
with open('top_players.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    for text in players_text:
        csvwriter.writerow([text])

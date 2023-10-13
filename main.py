from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import csv

chrome_driver_path = "C:\development\chromedriver.exe"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://sofifa.com/players")

# #Przełączenie na Iframe
# driver.switch_to.frame("googlefcLoaded")

#Zlokalizowanie przycisku akceptuj cookie
# cokie_accept_button = driver.find_element(By.CSS_SELECTOR, '.fc-cta-consent')
# cokie_accept_button.click()

sleep(2)


#Zlokalizowanie kolumny overall rating
overall_rating = driver.find_element(By.CSS_SELECTOR, 'th.col-oa[aria-label="Overall rating"]')
overall_rating.click()

#Utworzenie listy nazwisk
players_surname = driver.find_elements(By.CSS_SELECTOR, 'td.col-name > a[role="tooltip"] > div.ellipsis')

players_surname_text = []
for surname in players_surname[:15]:
    players_surname_text.append(surname.text)

print(players_surname_text)

#Utworzenie listy statystyk
players_rating = driver.find_elements(By.CSS_SELECTOR, 'td.col-oa[data-col="oa"]')

players_rating_text = []
for rating in players_rating[:15]:
    players_rating_text.append(rating.text)

# Zapisz nazwiska zawodników do pliku CSV
with open('nazwiska_zawodnikow.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    # Zapisz nagłówek, jeśli go potrzebujesz
    # csvwriter.writerow(['Nazwisko'])
    # Zapisz nazwiska zawodników
    for nazwisko in players_surname_text:
        csvwriter.writerow([nazwisko])


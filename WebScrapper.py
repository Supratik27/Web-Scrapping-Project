from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import pandas as pd
from selenium.webdriver.support.select import Select

# Importing the Firefox webdriver

service_obj = Service("C:\\Users\\Lenovo\\Downloads\\geckodriver-v0.32.2-win64\\geckodriver.exe")
driver = webdriver.Firefox(service=service_obj)
driver.get("https://www.adamchoi.co.uk/overs/detailed")
driver.implicitly_wait(4)
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "label[analytics-event='All matches']").click()

# Selecting the Football games data by Country Names
Name = input("Enter the country name which you want the football data for:")

dropdown = Select(driver.find_element(By.ID, "country"))
dropdown.select_by_visible_text(Name)

# Extracting Data from Website

games = driver.find_elements(By.TAG_NAME, 'tr')
Date = []
Score = []
Home_team = []
Away_team = []

for game in games:
    Date.append(game.find_element(By.XPATH, "./td[1]").text)
    Home_team.append(game.find_element(By.XPATH, "./td[2]").text)
    Score.append(game.find_element(By.XPATH, "./td[3]").text)
    Away_team.append(game.find_element(By.XPATH, "./td[4]").text)


# Exporting data to CSV file with Pandas

Data_frame = pd.DataFrame({'Date': Date, 'Home Team': Home_team, 'Scores': Score, 'Away Team': Away_team})
Data_frame.to_csv("FootBall_Data.csv", index=False)
print(Data_frame)
driver.quit()


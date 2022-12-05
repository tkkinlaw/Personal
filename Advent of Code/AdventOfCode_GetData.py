import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

"""
To use the function below:
- username = you GitHub username (string)
- password = your GitHub password (string)
- day = specify the number day you want the data for (integer)
- headless = do you want a chrome browser to open/close? (boolean)
- driverloc = install the appropriate chrome driver where your you place this python file
"""

def GetData_GitHubLogin(username, password, day, headless, driverLoc):
    dataUrlDay = os.path.join("https://adventofcode.com/2022/day", str(day), "input").replace("\\","/")
    url = "https://adventofcode.com"
    loginUrl = "https://adventofcode.com/2022/auth/login"
    chromeDriver = driverLoc
     
    options = Options()
    options.headless = headless
    options.add_argument("--window-size=1920,1200")

    driver = webdriver.Chrome(options=options, executable_path=chromeDriver)

    driver.get(url)
    driver.get(loginUrl)
    driver.find_element(By.XPATH, '/html/body/main/p[2]/a[1]').click()
    driver.find_element(By.ID, "login_field").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.NAME, "commit").click()
    driver.get(dataUrlDay)
    mytext = driver.find_element(By.XPATH, '/html/body/pre')
    data = mytext.text
    driver.quit()
    return data

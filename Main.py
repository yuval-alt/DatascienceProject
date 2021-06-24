from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
PATH = "/Users/carnegon.gaming/Documents/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://twitchtracker.com/channels/viewership?page=1")
data = []
try:
    for i in range(200):
        table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "channels"))
        )
        table = table.find_element_by_tag_name("tbody")
        channels = table.find_elements_by_tag_name("tr")
        for channel in channels:
            name = channel.find_elements_by_tag_name("td")
            l = []
            for n in name:
                if(n.text.splitlines() != []):
                    l.append(n.text.splitlines()[0])
            data.append(l)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        link = driver.find_element_by_link_text("NEXT")
        link.click()
finally:
    driver.quit()
    df = pd.DataFrame(data,columns=["number","name","AVG Views","Time Streamed","Peak","Hours Watched","Rank","Followers gaind","Total Followers","Total Views"])
    df.to_csv("Data3.csv")



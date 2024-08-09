from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up Chrome options to keep the page open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.in/POCO-Snowstorm-White-RAM-Storage/dp/B0CSDS6VGW/ref=sr_1_1_sspa?crid=3CYJSX1B91P16&dib=eyJ2IjoiMSJ9.1bEsT-Dne77Sx49DqQ7YvffbJYf6jUqIpkBL-wUdS_blMqdIqud53F8fkdsWcxizN4GGIqCs32-_TdDZlXTcsJi3Oj7Qz2lws8kvEKFUdOq_nsP5bgMiV7eNaKltC0tBc7IOhGmrNRabABlAbrCAcRMwffXsjMr7uVfiscajSyx5PYeNK7S6U6MT45CQOOgNo0tWRwfcgltL1Nz6YopCXveD9-8Wj_r1f6RigN7mLJM.tTQlwW05L3VmliJjibtc74c8EZUPPmPFBLvRUcxOxOQ&dib_tag=se&keywords=poco%2Bx6&qid=1723098993&sprefix=%2Caps%2C234&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1")

# Find price elements
price_link = driver.find_element(By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[3]/span[2]/span[2]')

price_symbol = driver.find_element(By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[3]/span[2]/span[1]')

# Print the price
print(f"The price is {price_symbol.text}{price_link.text}")

driver.quit()


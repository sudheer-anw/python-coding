from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up Chrome options to keep the page open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")
f_name = driver.find_element(By.XPATH,'/html/body/form/input[1]')
l_name = driver.find_element(By.XPATH,'/html/body/form/input[2]')
email = driver.find_element(By.XPATH,'/html/body/form/input[3]')
f_name.send_keys("sudheer")
l_name.send_keys("b")
email.send_keys("sud@gmail.com")

submit = driver.find_element(By.CSS_SELECTOR, value="form button")
submit.click()

driver.quit()

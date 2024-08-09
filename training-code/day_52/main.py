from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TARGET_ACCOUNT = "targated_user"  # Change this to the account you want to visit
USERNAME = "your id"
PASSWORD = "password"

# Initialize the WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)  # Initialize WebDriverWait once

def login():
    url = "https://www.instagram.com/accounts/login/"
    driver.get(url)

    try:
        # Wait for the cookie warning and decline if present
        decline_cookies_xpath = "//button[contains(text(), 'Only Essential')]"
        decline_cookies = wait.until(EC.element_to_be_clickable((By.XPATH, decline_cookies_xpath)))
        decline_cookies.click()
    except TimeoutException:
        pass  # Cookie warning not present

    # Log in
    username = driver.find_element(by=By.NAME, value="username")
    password = driver.find_element(by=By.NAME, value="password")
    username.send_keys(USERNAME)
    password.send_keys(PASSWORD)
    password.send_keys(Keys.ENTER)

    # Click "Not now" and ignore Save-login info prompt
    try:
        save_login_prompt = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]")))
        save_login_prompt.click()
    except TimeoutException:
        pass  # Save login prompt not present

    # Click "not now" on notifications prompt
    try:
        notifications_prompt = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]")))
        notifications_prompt.click()
    except TimeoutException:
        pass  # Notifications prompt not present

def open_target_account():
    target_account_url = f"https://www.instagram.com/{TARGET_ACCOUNT}/"
    driver.get(target_account_url)

# Run the script
login()
open_target_account()


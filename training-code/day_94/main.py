from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Setup the Chrome driver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Runs Chrome in headless mode.
chrome_service = Service('/usr/local/bin/chromedriver')  # Update this to your chromedriver path
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Open the Dino game in Chrome
driver = driver.get("chrome://dino")
print(driver)

# Give the page a little time to load
time.sleep(2)

# Start the game
body = driver.find_element("tag name", "body")
body.send_keys(Keys.SPACE)  # Start the game by pressing SPACE

def jump():
    body.send_keys(Keys.SPACE)

def keep_playing():
    while True:
        try:
            # Check if the game is in the "Game Over" state
            game_over_text = driver.find_element("xpath", '//*[contains(text(),"Game Over")]')
            if game_over_text:
                break
        except:
            pass

        # Simulate the Dino jumping
        jump()
        
        # Wait a bit before the next jump
        time.sleep(0.1)

keep_playing()

# Close the browser after the game ends
driver.quit()


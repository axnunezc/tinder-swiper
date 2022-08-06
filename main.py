from selenium import webdriver
from decouple import config
import time
from selenium.common.exceptions import NoSuchElementException

email = config("EMAIL")
password = config("PASSWORD")

chrome_driver_path = "/Users/axel/Documents/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

def get_buttons():
    buttons = driver.find_elements_by_xpath("//button[@draggable='false']")
    return buttons

# Open tinder
driver.get("https://tinder.com/")

time.sleep(2)

# Redirect to login page
driver.find_element_by_xpath(("//*[text()='Log in']")).click()

time.sleep(2)

# Click on "Log In with Facebook"
driver.find_element_by_xpath("//button[@aria-label='Log in with Facebook']").click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

time.sleep(2)

# Provide username
email_input = driver.find_element_by_xpath("//input[@name='email']")
email_input.send_keys(email)

# Provide password
password_input = driver.find_element_by_xpath("//input[@name='pass']")
password_input.send_keys(password)

# Click login button
driver.find_element_by_id("loginbutton").click()

driver.switch_to.window(base_window)
time.sleep(5)

# Allow location tracking
driver.find_element_by_xpath("//button[@aria-label='Allow']").click()
driver.find_element_by_xpath("//button[@aria-label='Not interested']").click()

# Get buttons
buttons = get_buttons()

# Accept cookies
buttons[5].click()

time.sleep(15)

# Get updated buttons
buttons = get_buttons()

for _ in range(100):
    time.sleep(3)
    
    # Click on Red X
    buttons[1].click()


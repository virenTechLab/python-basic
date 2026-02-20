import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# ------------------------------
# DRIVER SETUP
# ------------------------------

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)
actions = ActionChains(driver)

# ------------------------------
# OPEN WEBSITE
# ------------------------------

driver.get("https://the-internet.herokuapp.com/")
print("Title:", driver.title)
print("Current URL:", driver.current_url)

# ------------------------------
# NAVIGATION
# ------------------------------

driver.refresh()
driver.back()
driver.forward()

# ------------------------------
# CLICK + LOCATORS
# ------------------------------

driver.find_element(By.LINK_TEXT, "Form Authentication").click()

username = driver.find_element(By.ID, "username")
password = driver.find_element(By.NAME, "password")

username.send_keys("tomsmith")
password.send_keys("SuperSecretPassword!")

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# ------------------------------
# WAIT (Explicit)
# ------------------------------

wait.until(EC.presence_of_element_located((By.CLASS_NAME, "flash")))

# ------------------------------
# SCREENSHOT
# ------------------------------

driver.save_screenshot("login_success.png")

# ------------------------------
# COOKIES
# ------------------------------

print("Cookies:", driver.get_cookies())

# ------------------------------
# JAVASCRIPT EXECUTION
# ------------------------------

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# ------------------------------
# DROPDOWN
# ------------------------------

driver.get("https://the-internet.herokuapp.com/dropdown")
dropdown = Select(driver.find_element(By.ID, "dropdown"))
dropdown.select_by_visible_text("Option 1")

# ------------------------------
# ALERT HANDLING
# ------------------------------

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
alert = driver.switch_to.alert
print("Alert text:", alert.text)
alert.accept()

# ------------------------------
# FRAME HANDLING
# ------------------------------

driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
editor = driver.find_element(By.ID, "tinymce")
editor.clear()
editor.send_keys("Hello Selenium Frame!")
driver.switch_to.default_content()

# ------------------------------
# MULTIPLE WINDOWS
# ------------------------------

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()

windows = driver.window_handles
driver.switch_to.window(windows[1])
print("New Window Title:", driver.title)
driver.close()
driver.switch_to.window(windows[0])

# ------------------------------
# ACTION CHAINS (Hover)
# ------------------------------

driver.get("https://the-internet.herokuapp.com/hovers")
image = driver.find_element(By.CLASS_NAME, "figure")
actions.move_to_element(image).perform()
time.sleep(2)

# ------------------------------
# KEYBOARD ACTIONS
# ------------------------------

driver.get("https://the-internet.herokuapp.com/key_presses")
input_box = driver.find_element(By.ID, "target")
input_box.send_keys(Keys.ENTER)

# ------------------------------
# DRAG AND DROP
# ------------------------------

driver.get("https://the-internet.herokuapp.com/drag_and_drop")
source = driver.find_element(By.ID, "column-a")
target = driver.find_element(By.ID, "column-b")
actions.drag_and_drop(source, target).perform()

# ------------------------------
# EXCEPTION HANDLING
# ------------------------------

try:
    driver.find_element(By.ID, "not-existing")
except NoSuchElementException:
    print("Element not found!")

# ------------------------------
# CLOSE DRIVER
# ------------------------------

time.sleep(3)
driver.quit()

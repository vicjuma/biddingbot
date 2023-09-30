from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options)
driver.get("https://app.atlanticwriters.com/login")
email_field = driver.find_element(By.NAME, 'email')
password_field = driver.find_element(By.NAME, 'password')
email_field.send_keys('anneestherr45@gmail.com')
password_field.send_keys('Esther@2027')

login_button = driver.find_element(
    By.XPATH, '//button[text()="Login"]')
login_button.click()


def process_url(url):
    driver.get(url)
    print(url)
    wait = WebDriverWait(driver, 10)
    place_bid_button = wait.until(
        EC.presence_of_element_located(
            (By.XPATH,
             '//button[text()="Place bid"]')))
    place_bid_button.click()
    print(place_bid_button)


while True:
    sleep(1)
    driver.get("https://app.atlanticwriters.com/order/available")
    body = driver.find_element(By.TAG_NAME, 'body')
    actions = ActionChains(driver)
    order_row = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR,
             '[data-name="ExpertOrderRow"]')))
    status_element = order_row.find_element(
        By.XPATH, './/div[@data-name="Bids/Status"]')
    has_block_child = status_element.find_elements(
        By.XPATH, './div[@data-name="Block"]')
    link_element = order_row.find_element(
        By.XPATH,
        './/div[@data-name="icon > order/[id]"]/a')
    href = link_element.get_attribute('href')
    if not has_block_child:
        process_url(href)
    else:
        continue

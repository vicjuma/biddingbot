from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.keys import Keys

options = Options()
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(
    service=Service(
        ChromeDriverManager().install()),
    options=options)

driver.get("https://app.atlanticwriters.com/login")
email_field = driver.find_element(By.NAME, 'email')
password_field = driver.find_element(By.NAME, 'password')
email_field.send_keys('anneestherr45@gmail.com')
password_field.send_keys('Esther@2027')

# Locate and click the login button.
login_button = driver.find_element(By.XPATH, '//button[text()="Login"]')
login_button.click()

links = set()

while True:
    sleep(2)
    driver.get("https://app.atlanticwriters.com/order/available")

    wait = WebDriverWait(driver, 10)
    order_rows = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, '[data-name="ExpertOrderRow"]')))

    def process_url(url):
        driver.get(url)
        print(url)
        wait = WebDriverWait(driver, 10)  # Wait for a maximum of 10 seconds
        bid_prices_block = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//div[@data-name="BidPricesBlock"]')))
        print(bid_prices_block)

    for row in order_rows:
        status_element = row.find_element(
            By.XPATH, './/div[@data-name="Bids/Status"]')
        has_block_child = status_element.find_elements(
            By.XPATH, './div[@data-name="Block"]')
        link_element = row.find_element(
            By.XPATH, './/div[@data-name="icon > order/[id]"]/a')

        href = link_element.get_attribute('href')
        if href not in links:
            links.add(href)
        # else:
        #     continue

    for link in links:
        process_url(link)

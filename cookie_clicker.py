from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v85.input_ import MouseButton
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.proxy import Proxy, ProxyType, ProxyTypeFactory
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://orteil.dashnet.org/cookieclicker/')
time.sleep(5)

cookie_accept = driver.find_element(By.XPATH, '/html/body/div[1]/div/a[1]')
cookie_accept.click()

# https://orteil.dashnet.org/cookieclicker/

cookie_id = "bigCookie"
cookies_id = "cookies"
product_price_prefix = "productPrice"
product_prefix = "product"

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
)

language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, cookie_id))
)

cookie = driver.find_element(By.ID, cookie_id)

while True:
    cookie.click()
    cookies_count = driver.find_element(By.ID, cookies_id).text.split(" ")[0]
    cookies_count = int(cookies_count.replace(",", ""))

    for i in range(4):
        product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",", "")

        if not product_price.isdigit():
            continue

        product_price = int(product_price)

        if cookies_count >= product_price:
            product = driver.find_element(By.ID, product_prefix + str(i))
            product.click()
            break

#WebDriverWait(driver, 5).until(
#    EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/header/div/div/form/div[1]/input'))
#)

#ActionChains(driver).send_keys(Keys.RETURN).perform()

driver.quit()

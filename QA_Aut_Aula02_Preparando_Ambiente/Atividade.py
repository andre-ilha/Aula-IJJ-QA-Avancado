from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = Firefox()

link = 'https://google.com'

browser.get(link)

input_area = browser.find_element(By.NAME, "q")

input_area.send_keys('Instituto Joga Junto')
input_area.send_keys(Keys.ENTER)

result_search = browser.find_elements(By.TAG_NAME, 'h3')
print(result_search)

check = False

while result in result_search:
    if result.text == "Instituto Joga Junto":
        result.click()
        print("aeweee")
        check = True

title = browser.title

assert 'Instituto Joga Junto' in browser.title
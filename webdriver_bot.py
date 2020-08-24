from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import random
from selenium.webdriver.common.action_chains import ActionChains
import requests

def dropdown_selector(pos):
    drop_down = browser.find_elements(By.XPATH, "//select[starts-with(@id, 'cat-ajax question-category')]")
    select = Select(drop_down[pos])
    pos2 = random.randint(1,len(select.options)-1)
    select.select_by_index(pos2)
    
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

browser_profile = webdriver.FirefoxProfile()
browser_profile.set_preference("dom.webnotifications.enabled", False)
browser_profile.set_preference("dom.push.enabled", False)
browser = webdriver.Firefox(firefox_profile = browser_profile)
browser.get('https://www.etxa.com/wp-login.php')
browser.maximize_window()

username = browser.find_element_by_id("user_login")
username.clear()
username.send_keys("Gregg Thomps0n")

password = browser.find_element_by_id("user_pass")
password.clear()
password.send_keys("hrEFYSW3Fq4JMBm")

browser.find_element_by_id("wp-submit").click()

browser.get('https://www.etxa.com/add-question')

title_text = random_line('questions.txt')

elm = browser.find_elements(By.NAME, "title")
elm[1].send_keys(title_text)

dropdown_selector(1)
dropdown_selector(2)

r = requests.post("https://api.deepai.org/api/text-generator", data ={'text':random_line('questions.txt')}, headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'})
body = r.json()

elm2 = browser.find_elements(By.NAME, "comment")
elm2[1].send_keys(body['output'])


elem = browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/div/main/div/div[1]/div[5]/form/p/input[3]")

actions = ActionChains(browser)
actions.move_to_element(elem).perform()
elem.click()
#WebDriverWait(browser, 20).until(EC.element_is_visible((By.NAME, "title"))).send_keys("Text Test")

"""
js = "document.getElementsByName('title')[0].value = 'hello and good morning';"
browser.execute_script(js)
"""

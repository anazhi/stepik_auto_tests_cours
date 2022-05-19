from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math 



try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #x = value_x.text
    x = browser.find_element_by_id("num1")
    x1 = x.text
    y = browser.find_element_by_id("num2")
    y1 = y.text

    z = int(x1) + int(y1)
    z1 = str(z)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(z1) 
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
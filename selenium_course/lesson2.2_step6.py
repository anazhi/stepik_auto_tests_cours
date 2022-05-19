from selenium import webdriver
import time
import math 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("input_value")
    x1 = x.text

    #value_x = x1.text
    y = calc(x1)

    browser.execute_script("window.scrollBy(0, 100);")

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    checkbox1 = browser.find_element_by_id("robotCheckbox")
    checkbox1.click()

    radiobutton1 = browser.find_element_by_id("robotsRule")
    radiobutton1.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
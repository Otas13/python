# autologin funguje, prihlasi a otevre browser

from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys


def page_is_loaded(driver):
    return driver.find_element_by_tag_name("body") != None

def getInstructions():
    data = []
    file = open('instructions.txt', 'r')
    for x in range(0,5):
        data.append(file.readline().rstrip())

    return data

instructions = getInstructions()

driver = webdriver.Firefox()

# get page url from instruction file
driver.get(instructions[0])


wait = ui.WebDriverWait(driver, 10)

wait.until(page_is_loaded)

# login field name is on 2nd line of instruction script (starts with 0)
login_field = driver.find_element_by_name(instructions[1])

# insert user login from file, line 4
login_field.send_keys(instructions[3])

# password field name is on 3rd line
password_field = driver.find_element_by_name(instructions[2])

# user password is on line 5
password_field.send_keys(instructions[4])

password_field.send_keys(Keys.RETURN)
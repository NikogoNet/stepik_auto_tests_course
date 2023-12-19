from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
   return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    wait = WebDriverWait(browser,12)
    price = wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "$100")) 
    button = browser.find_element(By.ID, "book")
    button.click()
    
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    answer = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(y)
    
    buttonSubmit = browser.find_element(By.ID, 'solve')
    browser.execute_script("return arguments[0].scrollIntoView(true);", buttonSubmit)
    buttonSubmit.click()
    
    alert = browser.switch_to.alert
    print(alert.text)

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

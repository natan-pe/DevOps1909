from selenium import webdriver
from time import sleep

d = webdriver.Chrome()
d.get("file:///C:/Users/Natan%20Perlman/Downloads/tip_calc/tip_calc/index.html")
d.find_element(by="id", value="billamt").send_keys("200")
d.find_element(by="xpath", value='//*[@id="serviceQual"]/option[3]').click()
d.find_element(by="xpath", value='//*[@id="musicQual"]/option[5]').click()
d.find_element(by="id", value="peopleamt").send_keys("5")
d.find_element(by="id", value="calculate").click()
expected = "12.00"
actual = d.find_element(by="id", value="tip").text

if expected != actual:
    print("Test failed")
else:
    print("Test passed")
sleep(5)



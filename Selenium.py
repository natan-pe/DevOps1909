from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Set the path to ChromeDriver using Service
service = Service(r"C:\Windows\System32\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open Google and print feedback
print("Opening Google...")
driver.get("https://www.google.com")

# Find the search box and perform a search
print("Finding the search box and performing a search for 'Selenium Python'...")
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")
search_box.submit()

# Wait for 5 seconds to view the search results
print("Waiting 5 seconds to view the results...")
time.sleep(5)

# Close the browser with feedback
print("Closing the browser.")
driver.quit()

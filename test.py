from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

service = Service(r"C:\Program Files (x86)\chromedriver.exe")

driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)

def login(username, password):
    driver.get("https://katalon-demo-cura.herokuapp.com/profile.php#login")
    driver.maximize_window()
    driver.find_element(By.ID, "txt-username").send_keys(username)
    driver.find_element(By.ID, "txt-password").send_keys(password)
    driver.find_element(By.ID, "btn-login").click()
    

def go_to_appointment_calendar():
    driver.find_element(By.ID, "btn-make-appointment").click()
    

def book_appointment(date, time_slot):

    date_input = driver.find_element(By.ID, "txt_visit_date")
    date_input.clear()
    date_input.send_keys(date)
    date_input.send_keys(Keys.RETURN)
   
    driver.find_element(By.ID, "btn-book-appointment").click()

try:
    login("John Doe", "ThisIsNotAPassword")
    go_to_appointment_calendar()
    book_appointment("06/15/2024", "10:00 AM")
    print("Appointment booked successfully!")

finally:
    input("Enter the value to close it : \n")
    driver.quit()

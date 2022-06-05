# imports
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options # replace chrome with your browser
from pprint import PrettyPrinter
from user_data import *

# setup
printer = PrettyPrinter()
options = Options()
options.headless = True 
driver = webdriver.Chrome(options = options) # replace chrome with your browser

# code
def sleep(sec = 1):
    time.sleep(sec)
    # i was tired of typing time.sleep() every time, lol

driver.get(SCHOOL_URL)

sleep()

student = driver.find_element(By.ID, 'username')
student.send_keys(STUDENT_NUMBER)
student.submit()

sleep()

password = driver.find_element(By.ID, 'password')
password.send_keys(STUDENT_PASSWORD)
password.submit()

sleep()

print(f"succesfully logged into {SCHOOL_URL} using {str(STUDENT_NUMBER)}, {STUDENT_PASSWORD}")

sleep()

driver.get(SCHOOL_URL+"/magister/#/agenda")

sleep(5)

today = []
for course in range(MAX_COURSES):
    course_num = course + 1
    try:
        course_time = driver.find_element(By.XPATH, f'//*[@id="afsprakenLijst"]/div[2]/table/tbody/tr[{course_num}]/td[2]/span/span')
        course_info = driver.find_element(By.XPATH, f'//*[@id="afsprakenLijst"]/div[2]/table/tbody/tr[{course_num}]/td[3]/span/span[2]')
        course_location = driver.find_element(By.XPATH, f'//*[@id="afsprakenLijst"]/div[2]/table/tbody/tr[{course_num}]/td[3]/span/span[3]')
        course_info = [f'course {course}', course_time.text, course_info.text, course_location.text]
        today.append(course_info)
    except:
        if course != 0:
            break
        else:
            pass

driver.quit()

if today != []:
    printer.pprint(today)
else:
    print('    no data found\n    try setting your magister agenda view type to "afsprakenlijst"')
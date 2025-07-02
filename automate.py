import pyautogui
import time

course_name = input("Enter the course name to find the attendance: ")

chrome_icon_x = 700  
chrome_icon_y = 1044 

pyautogui.moveTo(chrome_icon_x, chrome_icon_y, duration=1)
pyautogui.click()
time.sleep(2)

pyautogui.hotkey('ctrl', 't')
time.sleep(1)
pyautogui.typewrite('lms')
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('enter')

login_button_x = 1844
login_button_y = 221
pyautogui.moveTo(login_button_x, login_button_y, duration=1)
pyautogui.click()
pyautogui.press('tab')

username = 'DS221002'
password = 'pakola123'
pyautogui.typewrite(username)
pyautogui.press('tab')
pyautogui.typewrite(password)

pyautogui.press('enter')
time.sleep(3)

course_x = 1291
course_y = 771
pyautogui.moveTo(course_x, course_y,duration=1)
pyautogui.click()
time.sleep(1)
pyautogui.click()
pyautogui.press('pagedown')

attendacne_x = 312
attendacne_y = 365
pyautogui.moveTo(attendacne_x, attendacne_y, duration=1)
pyautogui.click()
time.sleep(1)

all_courses_x = 397
all_courses_y = 610
pyautogui.moveTo(all_courses_x, all_courses_y, duration=1)
pyautogui.click()
time.sleep(3)
pyautogui.hotkey('ctrl', 'f')
pyautogui.typewrite(course_name)
pyautogui.press('enter')





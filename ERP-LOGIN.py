from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

driver = webdriver.Chrome(executable_path = r"C:\Drivers\chromedriver\chromedriver.exe")

driver.get("https://erp.mitwpu.edu.in/")                                       #Open the MIT-WPU ERP page
driver.maximize_window()                                                       #Maximize the window
time.sleep(.50)

uid = driver.find_element_by_name("txtUserId")                                 #Finding the element for erp id
uid.send_keys("S1234567890")                                                   #Typing the erp id
pwd = driver.find_element_by_name("txtPassword")                               #Finding the element for Password
pwd.send_keys("Password")                                                      #Typing the password

driver.save_screenshot("screenshot.png")                                       #Taking a screenshot
time.sleep(1)
img = Image.open('screenshot.png')
img2 = img.crop((1504,689,1688,748))                                           #Croping the Screenshot for Captcha  *The crop Area may vary according to the display size
text = pytesseract.image_to_string(img2)                                       #Using Tesseract to get the Captcha
print(text)
check = driver.find_elements_by_id("chkCheck")                                 #Finding the "I am not a Robot Check box"
check[0].click()                                                               #Checking the "I am not a Robot Check box"
captcha = driver.find_elements_by_xpath("//form/div[@id='UpdatePanel1']/div[@class='container-fluid']/div[@class='content-main']/div[@class='input-group']/input[@name='txtCaptcha']")      #Finding the Captcha Element
captcha[0].send_keys(text)                                                     #Typing the Captcha
login = driver.find_elements_by_name('btnLogin')                               #Finding the Log in Button
login[0].click()                                                               #Clicking the Log in Button
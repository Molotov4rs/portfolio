
from telnetlib import EC
from pyautogui import doubleClick
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pyautogui
import time
import datetime


#s=Service(ChromeDriverManager().install())
#driver = webdriver.Chrome(service=s)
#driver.maximize_window()
#options = Options()
#options.add_argument("start-maximized")
#options = webdriver.ChromeOptions()
#options.add_argument('--disable-extensions')
#options.add_argument('test-type')


def RSCHROME():
            
            BOTBYPASS = 0   
            print("Received")
            s=Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=s)
            driver.maximize_window()
            action = ActionChains(driver)
            driver.get("https://www.amazon.fr/ap/signin?clientContext=258-5705656-8801143&openid.pape.max_auth_age=3600&openid.return_to=https%3A%2F%2Flogistics.amazon.fr%2Fmarketing%2Fredirect-provider&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=amzl_logistics_fr&openid.mode=checkid_setup&marketPlaceId=A3DMTITTFNQK84&language=fr_FR&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
            #https://opfcaptcha-prod.s3.amazonaws.com/169dc8a2088e439a8c08ceae76f10e9b.jpg?AWSAccessKeyId=AKIA5WBBRBBBR4XLQCD6&Expires=1678065965&Signature=5ilSmtukilZ37aMCu%2FS%2FPJk0vno%3D
            link = 'https://www.amazon.fr/ap/signin/257-1325836-5176506'


            #driver.find_element(By.XPATH, '//button[text()="Some text"]')
            #driver.find_elements(By.XPATH, '//button')
            #driver = webdriver.Chrome(executable_path=r"C:\Users\ilmaa\Documents\RSBOT - Copie\chromedriver.exe")
        
            #driver.find_element(By.CLASS_NAME,"link").click()
            #driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div[1]/div/div[1]/div/header/div/div/div[3]/a").click()
            login1 = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/form/div/div/div/div[1]/input')
            login1.send_keys('blackbtsassu@gmail.com')
            password1 = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/form/div/div/div/div[2]/input')
            password1.send_keys('Pythonmaster1!')
            button1 = driver.find_element(By.ID,"signInSubmit")
            button1.click()
            time.sleep(1)
            password2 = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/form/div/div/div/div[2]/input')
            password2.send_keys('Pythonmaster1!')
            button2 = driver.find_element(By.ID,"signInSubmit")
            button2.click() 
            #BOTBYPASS2 = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/form/div/div/div/div[3]/div[2]/a')
            print("BYPASS BOT CONTINUE") 
            #if BOTBYPASS2 == BOTBYPASS2:
                    #captcha = AmazonCaptcha.fromdriver('https://www.amazon.fr/ap/signin/257-1325836-5176506')
                    #solution = captcha.solve()
                    #print("BOT BLOCK")
                    #quit()
           
            
            time.sleep(2)
            RS6 = pyautogui.screenshot(r'C:\Users\ilmaa\Documents\RSBOT BETACOPIE - Copie\11.png')
            print("! RSSCREENSHOT TAKEN !")
                    
            #RS6 = pyautogui.screenshot(r"C:\Users\ilmaa\Documents\RSBOT BETACOPIE - Copie\11.png")
            #cookie_button = driver.find_element(By.CLASS_NAME, "awsccc-u-btn awsccc-u-btn-primary")



            while True:
                 pass
RSCHROME()

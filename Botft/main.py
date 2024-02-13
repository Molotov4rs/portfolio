from selenium import webdriver  
from selenium.webdriver.chrome.webdriver import WebDriver   
from selenium.webdriver.common.action_chains import ActionChains    
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
import time 
import os 
import sys 
import requests 
from bs4 import BeautifulSoup





def chromeBOT():
    driver: WebDriver = webdriver.Chrome()
    driver.get('https://www.pole-emploi.fr/accueil/')
    driver.implicitly_wait(2)
    driver.get_window_size(max)

    cookiebar = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/button[2]")
    cookiebar.click()
    time.sleep(1)

    login1 = driver.find_element(By.XPATH,"/html/body/app-root/app-header/header/div/ul/li[1]/div/button/span[1]")
    login1.click()
    time.sleep(1)

    login2 = driver.find_element(By.XPATH,"/html/body/app-root/app-header/header/div/ul/li[1]/div/ul/li[1]/a")
    login2.click()
    time.sleep(1)

    time.sleep(3)
    idbar = driver.find_element(By.XPATH,"/html/body/div[2]/div/main/div[1]/div/form/div[1]/input")
    time.sleep(1)
    idbar.send_keys('')
    time.sleep(1)

    idbar2 = driver.find_element(By.XPATH,"/html/body/div[2]/div/main/div[1]/div/form/div[3]/button[1]")
    idbar2.click()
    time.sleep(1)

    idbar3 = driver.find_element(By.XPATH,"/html/body/div[2]/div/main/div[1]/div/form/div[2]/input")
    time.sleep(1)
    idbar3.send_keys('')
    time.sleep(1)


    loginbutton = driver.find_element(By.XPATH,"/html/body/div[2]/div/main/div[1]/div/form/div[4]/button[1]")
    time.sleep(1)
    loginbutton.click()
    
    time.sleep(2)
    searchbar1 = driver.find_element(By.XPATH,"/html/body/app-root/ng-component/cl-layout/main/app-accueil/div/div[2]/div/div/div[1]/div/div[1]/pn-menu-navigation/div[1]/div/ul/li[3]/div/button")
    searchbar1.click()
    time.sleep(1)

    searchbar2 = driver.find_element(By.XPATH,"/html/body/app-root/ng-component/cl-layout/main/app-accueil/div/div[2]/div/div/div[1]/div/div[1]/pn-menu-navigation/div[1]/div/ul/li[3]/div/div/div/ul/li[1]/a/span[1]")
    time.sleep(1)
    searchbar2.click()

    time.sleep(3)
    worksearchbar1 = driver.find_element(By.XPATH,"/html/body/app-root/app-main/cl-layout/main/app-landing/div/div/div[1]/div/app-bloc-recherche-offre/div/div[2]/div/div/div[1]/div/div[2]/div[1]/input")
    time.sleep(2)
    worksearchbar1.send_keys('Alternance Technicien Informatique')

    worksearchbar2 = driver.find_element(By.XPATH,"/html/body/app-root/app-main/cl-layout/main/app-landing/div/div/div[1]/div/app-bloc-recherche-offre/div/div[2]/div/div/div[2]/div/div[2]/div[1]/input")
    time.sleep(2)
    worksearchbar2.send_keys('66000 PERPIGNAN')

    time.sleep(2)
    workbutton1 = driver.find_element(By.XPATH, "/html/body/app-root/app-main/cl-layout/main/app-landing/div/div/div[1]/div/app-bloc-recherche-offre/div/div[2]/div/button/span[1]")
    time.sleep(3)
    workbutton1.click()


    time.sleep(2)
    workbutton3 = driver.find_element(By.XPATH, "/html/body/main/div[1]/div[1]/div/div[2]/div/form/div[2]/ul/li[1]/div/input")
    time.sleep(2)
    workbutton3.click()

    time.sleep(1)
    workbutton4 = driver.find_element(By.XPATH, "/html/body/main/div[1]/div[1]/div/div[2]/div/form/div[2]/ul/li[7]/button")
    workbutton4.click()


    time.sleep(3)
    filter1 = driver.find_element(By.XPATH, "/html/body/main/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[1]/div[1]/div/div/button")
    time.sleep(2)
    filter1.click()

    filter2 = driver.find_element(By.XPATH, "/html/body/main/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[1]/div[1]/div/div/ul/li[2]/a")
    time.sleep(2)
    filter2.click()

    r = requests.get("https://candidat.pole-emploi.fr/offres/recherche?motsCles=Alternance+Technicien+Informatique&offresPartenaires=true&range=0-19&rayon=10&tri=0")
    print(r.status_code)
    urls = []
    page_number = 1

    for i in range(2):
        i = "https://candidat.pole-emploi.fr/offres/recherche?motsCles=Alternance+Technicien+Informatique&offresPartenaires=true&range=0-19&rayon=10&tri=0"
        page_number += 1 
        urls.append(i)
        return urls 
    
    r = requests.get("https://candidat.pole-emploi.fr/offres/recherche?motsCles=Alternance+Technicien+Informatique&offresPartenaires=false&range=0-19&rayon=10&tri=1")
    soup = BeautifulSoup(r.content,"html parser")
    print(soup)





    #joblist = driver.find_element(By.XPATH, "/html/body/main/div[1]/div[2]/div[1]/div/div[2]/div[2]/ul[1]/li[1]/a[1]/div[2]/h2/span[1]")
    #time.sleep(1)
    #joblist.click()
    
    while True:
        pass










chromeBOT()

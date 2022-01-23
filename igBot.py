from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class InstagramBot:
    
 
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
    
    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(3)

 #btn_login
        campo_usuario= driver.find_element_by_xpath("//input[@name='username']")
        campo_usuario.click()
        campo_usuario.clear()
        campo_usuario.send_keys(self.username)

#bnt_senha
        campo_senha = driver.find_element_by_xpath("//input[@name='password']")
        campo_senha.click()
        campo_senha.clear()
        campo_senha.send_keys(self.password)
        campo_senha.send_keys(Keys.ENTER)

        time.sleep(5)
        self.comentar('viagens')

    @staticmethod
    def digite_como_pessoa(frase,ondeDigitar):
        for letra in frase:
            ondeDigitar.send_keys(letra)
            time.sleep(random.randint(1,5)/30)

         
    def comentar(self,hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/"+ hashtag +"/")

        for i in range(1,3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)
        
        hrefs= driver.find_elements_by_tag_name('a')
        pic_hefs = [elem.get_attribute('href')for elem in hrefs]
        [href for href in pic_hefs if hashtag in href]
        print(hashtag +'fotos'+ str(len(pic_hefs)))

        for pic_href in pic_hefs:
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                comentarios=["Top","Show","😁","🤩"]
                driver.find_element_by_class_name('Ypffh').click()
                campo_comentario= driver.find_element_by_class_name('Ypffh')
                time.sleep(random.randint(2,5))
                self.digite_como_pessoa(random.choice(comentarios), campo_comentario)
                time.sleep(random.randint(30,120))
                driver.find_element_by_xpath( "//button[contains(text(),'Publicar')]").click()
                time.sleep(5)

            except Exception as e:
                print(e)
                time.sleep(5)
 
nomeBot = InstagramBot('loginValido','senhaValida')
nomeBot.login()
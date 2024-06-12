from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import os

options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=options)

class WSFM:
    def __init__(self, driver, user, password):
        self.driver = driver
        self.logado = False
        self.user = user
        self.password = password

        self.logar()

    def abrir(self, pagina):
        if self.logado == True:
            self.driver.get(f"https://site.url/#{pagina}")
            sleep(0.5)
        
    def logar(self):
        try:
            self.driver.get(f"https://site.url")
            self.esperar_escrever("//input[@id='formUsername-inputEl']", self.user, False)
            self.esperar_escrever("//input[@id='formPassword-inputEl']", self.password, False)
            self.esperar_clicar("//span[@id='loginButton-btnEl']")
            self.esperar_existir("//img[@src='/Images/brand.svg']")
            self.logado = True
        except:
            print("ERRO: Falha ao tentar fazer login!")

  
    def esperar_clicar(self, elemento):
        try:
            WebDriverWait(self.driver, 60).until( 
                EC.presence_of_element_located((By.XPATH, elemento))
            ).click()
            sleep(0.1)
        except:
            print("ERRO: esperar_clicar()")
    

    def esperar_apagar_texto(self, elemento):
        try:
            WebDriverWait(self.driver, 60).until( 
                EC.presence_of_element_located((By.XPATH, elemento))
            ).send_keys(Keys.CONTROL + "A" + Keys.DELETE)
            sleep(0.8)
        except:
            print("ERRO: esperar_apagar_texto()")


    def esperar_escrever(self, elemento, texto, enter):
        try:
            elemento_existente = WebDriverWait(self.driver, 60).until( 
                EC.presence_of_element_located((By.XPATH, elemento))
            )

            sleep(0.8)
            elemento_existente.send_keys(texto)
            if enter == True:
                elemento_existente.send_keys(Keys.ENTER)

            sleep(0.1)
        except:
            print("ERRO: esperar_escrever()")


    def esperar_existir(self, elemento):
        try:
            WebDriverWait(self.driver, 60).until( 
                EC.presence_of_element_located((By.XPATH, elemento))
            )
            sleep(0.1)
        except:
            print("ERRO: esperar_existir()")

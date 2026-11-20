from selenium import webdriver
import time

# abrir o navegador
navegador = webdriver.Chrome()

# acessar um site
navegador.get("https://www.hashtagtreinamentos.com/")

# colocar o navegador em tela cheia
navegador.maximize_window()

# selecionar um elemento na tela
botao_verde = navegador.find_element("class name", "botao-verde")

# clicar em um elemento
botao_verde.click()

# encontrar varios elementos
lista_botoes = navegador.find_elements("class name", "header__titulo")

for botao in lista_botoes:
    if "Assinatura" in botao.text:
        botao.click()
        break
    

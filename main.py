from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl
from datetime import datetime
import os
import time

# Caminho da planilha
EXCEL_PATH = "temperatura.xlsx"

def inicializar_planilha():
    """Cria a planilha e cabeçalho caso ainda não exista."""
    if not os.path.exists(EXCEL_PATH):
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.append(["Data/Hora", "Temperatura", "Umidade do Ar"])
        wb.save(EXCEL_PATH)

def capturar_temperatura():
    """Função acionada pelo botão da interface.
    - Abre navegador headless
    - Captura temperatura e umidade do site Climatempo
    - Salva os dados na planilha Excel
    """
    status_label.config(text="Buscando...")

    # Inicializa planilha se necessário
    inicializar_planilha()

    # Opções do navegador
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")

    # Ajuste o caminho do chromedriver se necessário
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/558/saopaulo-sp")
        time.sleep(5)  # Pequeno delay para garantir carregamento

        temperatura = driver.find_element(By.CLASS_NAME, "temperature").text
        umidade = driver.find_element(By.XPATH, '//span[contains(text(),"Umidade")]/following-sibling::span').text
        datahora = datetime.now().strftime("%d/%m/%Y %H:%M")

        wb = openpyxl.load_workbook(EXCEL_PATH)
        ws = wb.active
        ws.append([datahora, temperatura, umidade])
        wb.save(EXCEL_PATH)

        status_label.config(text=f"Captura realizada com sucesso às {datahora}")
    except Exception as e:
        status_label.config(text=f"Erro: {e}")
    finally:
        driver.quit()

# ---------- Interface ----------
inicializar_planilha()

janela = Tk()
janela.title("Captador de Temperatura - São Paulo")

Label(janela, text="Clique no botão abaixo para captar os dados:").pack(pady=10)
Button(janela, text="Buscar Previsão", command=capturar_temperatura).pack(pady=10)
status_label = Label(janela, text="")
status_label.pack(pady=10)

janela.mainloop()

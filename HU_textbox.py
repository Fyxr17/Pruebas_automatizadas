from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import os
import pytest

def inicializar_driver():
    return webdriver.Firefox()

def llenar_formulario(driver):
    driver.get("https://demoqa.com/text-box")

    nombre_completo = driver.find_element(By.ID, "userName")
    nombre_completo.send_keys("Juan")

    correo = driver.find_element(By.ID, "userEmail")
    correo.send_keys("JuanPedro13@gmail.com")

    direccion_actual = driver.find_element(By.ID, "currentAddress")
    direccion_actual.send_keys("alma rosa")

    direccion_permanente = driver.find_element(By.ID, "permanentAddress")
    direccion_permanente.send_keys("santo domingo")

def enviar_formulario(driver):
    boton_enviar = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].click();", boton_enviar)

def capturar_pantalla(driver, nombre_archivo):
    driver.save_screenshot(nombre_archivo)

def cerrar_driver(driver):
    driver.quit()

def test_llenar_y_enviar_formulario():
    driver = inicializar_driver()

    try:
        llenar_formulario(driver)
        enviar_formulario(driver)
        capturar_pantalla(driver, "captura_de_pantalla.png")

    finally:
        cerrar_driver(driver)

if __name__ == "__main__":
    pytest.main(['-v', '--html=reporte.html'])
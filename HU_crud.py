import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import os

def initialize_driver():
    # Inicializar el driver
    driver = webdriver.Firefox()
    return driver

def navigate_to_website(driver):
    # 4-Como usuario, quiero poder añadir, editar y eliminar datos de una tabla.
    driver.get("https://demoqa.com/webtables")

def delete_existing_records(driver):
    # Eliminar los registros existentes
    boton_eliminar = driver.find_element(By.ID, "delete-record-1")
    boton_eliminar.click()
    boton_eliminar = driver.find_element(By.ID, "delete-record-2")
    boton_eliminar.click()
    boton_eliminar = driver.find_element(By.ID, "delete-record-3")
    boton_eliminar.click()

def add_new_record(driver):
    # Añadir un nuevo registro
    boton_añadir = driver.find_element(By.ID, "addNewRecordButton")
    boton_añadir.click()

    # Rellenar los campos del formulario
    nombre = driver.find_element(By.ID, "firstName")
    nombre.send_keys("Marcos")
    apellido = driver.find_element(By.ID, "lastName")
    apellido.send_keys("Ogando")
    correo = driver.find_element(By.ID, "userEmail")
    correo.send_keys("correo@ejemplo.com")
    edad = driver.find_element(By.ID, "age")
    edad.send_keys("20")
    salario = driver.find_element(By.ID, "salary")
    salario.send_keys("10000")
    departamento = driver.find_element(By.ID, "department")
    departamento.send_keys("Desarrollo")

    # Enviar el formulario
    boton_enviar = driver.find_element(By.ID, "submit")
    boton_enviar.click()

    # Esperar 5 segundos para visualisar 
    sleep(5)

def edit_existing_record(driver):
    # Editar un registro existente
    boton_editar = driver.find_element(By.ID, "edit-record-1")
    boton_editar.click()

    # Actualizar los campos del formulario
    nombre = driver.find_element(By.ID, "firstName")
    nombre.clear()
    nombre.send_keys("Gabriel")
    apellido = driver.find_element(By.ID, "lastName")
    apellido.clear()
    apellido.send_keys("Rosario")
    correo = driver.find_element(By.ID, "userEmail")
    correo.clear()
    correo.send_keys("nuevo@ejemplo.com")
    edad = driver.find_element(By.ID, "age")
    edad.clear()
    edad.send_keys("19")
    salario = driver.find_element(By.ID, "salary")
    salario.clear()
    salario.send_keys("20000")
    departamento = driver.find_element(By.ID, "department")
    departamento.clear()
    departamento.send_keys("QA")

    # Enviar el formulario
    boton_enviar = driver.find_element(By.ID, "submit")
    boton_enviar.click()

    # Esperar 5 segundos para visualisar 
    sleep(5)

def capture_screenshot(driver):
    # Capturar y guardar una captura de pantalla
    driver.save_screenshot("captura_de_pantalla.png")

def close_driver(driver):
    # Cerrar el driver
    driver.quit()

def test_webtable_manipulation():
    driver = initialize_driver()
    navigate_to_website(driver)
    delete_existing_records(driver)
    add_new_record(driver)
    edit_existing_record(driver)
    capture_screenshot(driver)
    close_driver(driver)

if __name__ == "__main__":
    pytest.main(["-v", "--html=report.html"])

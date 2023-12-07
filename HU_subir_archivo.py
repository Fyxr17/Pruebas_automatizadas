import os
import time
import pytest
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def driver():
    # Inicia el navegador
    driver = webdriver.Chrome()
    yield driver
    # Cierra el navegador después de la prueba
    driver.quit()

def test_file_download_and_upload_and_screenshot(driver):
    # Navega a la página
    driver.get("https://demoqa.com/upload-download")

    # Realiza acciones en la página
    download_link = driver.find_element(By.ID, "downloadButton")
    download_link.click()

    # Espera a que se complete la descarga (puedes ajustar esto según sea necesario)
    time.sleep(5)  # Puedes ajustar el tiempo de espera según sea necesario

    # Simula la búsqueda y selección del archivo descargado
    file_path = os.path.join(os.getcwd(), "sampleFile.jpeg")  # Cambia "sample.txt" al nombre del archivo descargado
    pyautogui.write(file_path)
    pyautogui.press("enter")

    # Captura de pantalla después de la descarga
    screenshot_path_download = os.path.join(os.getcwd(), "screenshot_download.png")
    driver.save_screenshot(screenshot_path_download)

    # Verifica que la descarga fue exitosa
    assert os.path.exists(screenshot_path_download)

    # Subir archivo (verificar que la ruta donde se descargo sea la correcta)
    ruta_archivo_descargado = "C:\\Users\\user\\Downloads\\sampleFile.jpeg"
    boton_subir = driver.find_element(By.ID, "uploadFile")
    boton_subir.send_keys(ruta_archivo_descargado)
    
    # Espera a que se complete la carga (puedes ajustar esto según sea necesario)
    time.sleep(5)  # Puedes ajustar el tiempo de espera según sea necesario

    # Captura de pantalla después de la carga
    screenshot_path_upload = os.path.join(os.getcwd(), "screenshot_upload.png")
    driver.save_screenshot(screenshot_path_upload)

    # Verifica que la carga fue exitosa
    assert os.path.exists(screenshot_path_upload)

if __name__ == "__main__":
    # Ejecuta la prueba con pytest y genera el informe en HTML
    pytest.main(['-v', '--html=reporte.html'])

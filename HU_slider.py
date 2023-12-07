import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def inicializar_driver():
    return webdriver.Firefox()

def abrir_url(driver, url):
    driver.get(url)

def encontrar_elemento_por_id(driver, element_id):
    return driver.find_element(By.ID, element_id)

def mover_control_deslizante(driver, slider_element, offset_x, offset_y):
    acciones = ActionChains(driver)
    acciones.click_and_hold(slider_element).move_by_offset(offset_x, offset_y).release().perform()

def capturar_screenshot(driver, filename):
    driver.save_screenshot(filename)

def cerrar_driver(driver):
    driver.quit()

# Función para generar un informe HTML con pytest
def generar_reporte_html(nombre_reporte):
    pytest.main(["-v", "--html=" + nombre_reporte])

# Función de prueba
@pytest.mark.prueba_web
def test_mover_control_deslizante():
    driver = inicializar_driver()

    try:
        # 3-Como usuario, quiero poder mover un control deslizante.
        abrir_url(driver, "https://demoqa.com/slider")

        # Encontrar el control deslizante
        deslizador = encontrar_elemento_por_id(driver, "sliderContainer")

        # Crear una acción de arrastre y soltura y ejecutarla
        mover_control_deslizante(driver, deslizador, 40, 0)

        # Capturar y guardar una captura de pantalla
        capturar_screenshot(driver, "captura_de_pantalla.png")

    finally:
        # Cerrar el driver al finalizar
        cerrar_driver(driver)

# Uso de la función para generar el informe HTML
generar_reporte_html("informe_pruebas_web.html")
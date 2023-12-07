import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

def test_seleccionar_fecha_y_capturar_screenshot(request, driver):
    # Abre la página y realiza las acciones
    driver.get("https://demoqa.com/date-picker")

    campo_fecha = driver.find_element(By.ID, "datePickerMonthYearInput")
    campo_fecha.clear()
    campo_fecha.send_keys("05/12/2012")

    sleep(2)  # Agrega una pausa para que puedas ver la página antes de que se cierre

    # Captura de pantalla
    driver.save_screenshot("captura_de_pantalla.png")

    # Agrega un mensaje al informe HTML
    mensaje_informe = "Se ha completado la selección de fecha y captura de pantalla."

    # Utiliza la función de Pytest para agregar información al informe HTML
    pytest_html = request.config.pluginmanager.get_plugin("html")
    if pytest_html is not None:
        extra = getattr(request.config, '_html_extra', [])
        extra.append("<p>{}</p>".format(mensaje_informe))
        request.config._html_extra = extra

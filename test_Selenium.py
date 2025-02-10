# test_selenium.py
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def test_google_search():
    # Configura el WebDriver para usar Google Chrome
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Abre Google
        driver.get("https://www.google.com")

        # Encuentra el campo de búsqueda y realiza una búsqueda
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Selenium WebDriver")
        search_box.submit()

        # Espera un poco para que se carguen los resultados
        time.sleep(2)

        # Verifica si los resultados de la búsqueda contienen el término buscado
        assert "Selenium WebDriver" in driver.title
    finally:
        # Cierra el navegador
        driver.quit()

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuración del navegador
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920,1080")

# Ruta del ChromeDriver en GitHub Actions
chrome_options.binary_location = "/usr/bin/google-chrome"
service = Service("/usr/bin/chromedriver")

MOODLE_URL = "https://cursos2.e-itesca.edu.mx/2025-I/login/index.php"
USERNAME = "21130376"
PASSWORD = "37CSF"

def marcar_asistencia():
    try:
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get(MOODLE_URL)

        # Esperar hasta que los elementos de usuario y contraseña estén disponibles
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys(USERNAME)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(PASSWORD)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "loginbtn"))).click()

        # Ir a la página de asistencia
        driver.get("https://cursos2.e-itesca.edu.mx/2025-I/mod/attendance/view.php?id=219")  

        # Buscar y hacer clic en "Enviar asistencia"
        enviar_asistencia = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Enviar asistencia"))
        )
        enviar_asistencia.click()

        # Esperar a que aparezcan los radio buttons
        presente_radio = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='radio' and @value='1']"))
        )
        presente_radio.click()

        # Hacer clic en "Guardar cambios"
        guardar_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Guardar cambios')]"))
        )
        guardar_btn.click()

        print("Asistencia marcada correctamente. :D")

    except Exception as e:
        print("Error al marcar asistencia:", e)

    finally:
        driver.quit()  # Cerrar el navegador después de cada ejecución

# Ejecutar la función inmediatamente
marcar_asistencia()

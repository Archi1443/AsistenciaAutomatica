from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import schedule 
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
MOODLE_URL = "https://cursos2.e-itesca.edu.mx/2025-I/login/index.php"
USERNAME = "21130376"
PASSWORD = "37CSF"

def marcar_asistencia():
    try:
        driver.get(MOODLE_URL)
        time.sleep(2) 
        driver.find_element(By.ID, "username").send_keys(USERNAME)
        driver.find_element(By.ID, "password").send_keys(PASSWORD)
        driver.find_element(By.ID, "loginbtn").click()
        time.sleep(3)
        driver.get("https://cursos2.e-itesca.edu.mx/2025-I/mod/attendance/view.php?id=219")  
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Presente')]").click()
        time.sleep(2)
        print("Asistencia marcada correctamente. :D")

    except Exception as e:
        print("Error xd:", e)

    finally:
        driver.quit()


schedule.every().monday.at("12:01").do(marcar_asistencia)
schedule.every().wednesday.at("12:01").do(marcar_asistencia)

while True:
    schedule.run_pending()
    time.sleep(60)

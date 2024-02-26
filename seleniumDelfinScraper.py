from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.options import BaseOptions
from selenium.webdriver import FirefoxOptions
from bs4 import BeautifulSoup
import csv

# Abrir navegador
# options = Options()
# options.set_preference("browser.download.folderList", 2)
# options.set_preference("browser.download.manager.showWhenStarting", False)
# options.set_preference("browser.download.dir", './proyectosComp')
# options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
# driver = webdriver.Firefox(options=options)

# Entrar a la página y hacer login
driver = webdriver.Firefox()
driver.get("https://programadelfin.org.mx/usuarios/inicio-registroestudiante-abrir.php")
username = driver.find_element(By.ID, "login")
password = driver.find_element(By.ID, "pass")

username.send_keys("ompacheco")
password.send_keys("hdjp7635")

login_button = driver.find_element(By.ID, "boton")
login_button.click()

# Entrar al directorio de asesores
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "DIRECTORIO DE ASESORES")))
link = driver.find_element(By.PARTIAL_LINK_TEXT, "DIRECTORIO DE ASESORES")
link.click()

# wait.until(EC.element_to_be_selected(areaElement))
for x in range (1,33):
  # Fill out the form
  areaElement = driver.find_element(By.ID, "id_area") # Fill area
  wait.until(EC.visibility_of(areaElement))
  area = Select(areaElement)
  area.select_by_value("00007")

  modalidadElement = driver.find_element(By.ID, "id_tasi") # Fill modalidad
  wait.until(EC.visibility_of(modalidadElement))
  modalidad = Select(modalidadElement)
  modalidad.select_by_value("00001")

  estadoElement = driver.find_element(By.ID, "id_edo") # Fill estado
  wait.until(EC.visibility_of(estadoElement))
  estado = Select(estadoElement)
  posiblesEstados = estado.options

  print(x)
  estado.select_by_index(x)
  estadoActual = estado.options[x].text
  print(estadoActual)

  # Submit the form
  wait.until(EC.element_to_be_clickable(driver.find_element(By.ID, "boton")))
  driver.find_element(By.ID, "boton").click()

  try:
    # Wait for the page to load or for specific elements to be available
    wait.until(EC.presence_of_element_located((By.ID, "tabla")))
  except TimeoutException:
    print("No se encontraron resultados")

  fichasProyectos = driver.get_downloadable_files()
  print(fichasProyectos)
  file_path = "proyectosComp/proyectos" + estadoActual
  html_file_path = file_path + ".html"
  file_html = open(html_file_path, "w", newline="", encoding="utf-8")

  # Extract the data
  html_content = driver.page_source

  # Process the HTML content as needed
  file_html.write(html_content)
  soup = BeautifulSoup(html_file_path, "html_parser")

  table = soup.find("table", {"id": "tabla"})

  csv_file_path = file_path + ".csv"
  csvfile = open(csv_file_path, "w", newline="", encoding="utf-8")
  csvwriter =csv.writer(csvfile)
  # for row in table.find_all("tr", ):

  file_html.close()

# Close the browser
driver.quit()

from bs4 import BeautifulSoup
import requests

# actionURL = "inicio-catalogoasesores-ver.php#encontrados"
actionURL = "https://programadelfin.org.mx/usuarios/inicio-catalogoasesores-ver.php#encontrados"

requests_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:122.0) Gecko/20100101 Firefox/122.0',
    'Referer': 'https://programadelfin.org.mx/usuarios/inicio-catalogoasesores-ver.php',
    'Cookie': 'delfin2024=e027f4d164ffbdf76c3dc933bfd2ab91',  # Update this value with a current session cookie if necessary
}

form_data = {
  'id_area': '00001',  # Example: Área I: Física, Matemáticas y Ciencias de la Tierra
  'id_tasi': '00001',  # Example: Presencial
  # 'id_insti': '00002',  # Example: Benemérita Universidad Autónoma de Puebla
  'id_edo': '00015',  # Example: Aguascalientes
}

response = requests.post(actionURL, headers=requests_headers, data=form_data)

if response.status_code == 200:
  print("Success")
  file_html = open("delfin.html", "w", newline="", encoding="utf-8")
  file_html.write(response.text)
  file_html.close()
else:
  print("Error")

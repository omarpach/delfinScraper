from bs4 import BeautifulSoup
import requests
import csv

paginaDelfin = requests.get("https://programadelfin.org.mx/usuarios/inicio-catalogoasesores-ver.php")
soup = BeautifulSoup(paginaDelfin.text, 'html.parser')

table_rows = soup.find_all('tr')

file = open("delfin.csv", "w", newline="", encoding="utf-8")
fileHTML = open("delfin.html", "w", newline="", encoding="utf-8")
fileHTML.write(paginaDelfin.text)
# file.write(paginaDelfin.text)
writer = csv.writer(file)

writer.writerow(["Modalidad"])

for row in table_rows:
    modalidad = soup.find_all("strong", attrs={"style": "color: #060;"})    # Extract information from each row
    # writer.writerow([modalidad.text])
    # ... and write it to the file
file.close()    # Close the file

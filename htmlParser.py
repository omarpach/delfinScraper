from bs4 import BeautifulSoup
import csv

htmlFile = open("proyectosComp/proyectosJalisco.html", "r", newline="", encoding="utf-8")
soup = BeautifulSoup(htmlFile, "html.parser")
# csvFile = open("proyectosComp/proyectosJalisco.csv", "w", newline="", encoding="utf-16")
# writer = csv.writer(csvFile)
htmlFile.close()
# writer.writerow(["Número","Investigador", "Modalidad", "Grado", "Ubicación", "Institución", "Área", "# de estudiantes a recibir", "Ficha", "Lineas de investigación"])

table = soup.find("table", {"id": "tabla"})
tableData = []
rowData = []

for row in soup.find_all("tr"):
  columns = []
  for col in row.find_all("td"):
    columns.append(col.contents)
  rowData.append(columns)

rowData.pop(0)
rowData.pop(0)

for row in rowData:
  cleanRow = []
  cleanRow.append(row[0])
  cleanColumns = []
  columns = row[1]
  auxList = []
  for col in columns:
    col_contents = col.contents
    for col_content in col_contents:
      auxList.append(col_content.string.text)

row_zero = rowData[12]
columns = row_zero[1]
columns.pop()

list1 = []
for col in columns:
  col_contents = col.contents
  # print(col_contents)
  list2 = []
  for col_content in col_contents:
    list2.append(col_content.string.text)
  list1.append(list2)
print(list1)
list1[0].pop(1)
for x in range(2,7):
  list1[x].pop(0)

list3 = []
for list in list1:
  list3.append(list[0])
# print(list3)

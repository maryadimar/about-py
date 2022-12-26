#--------------------------------------------
# Dibuat oleh maryadi
# pada 26/12/2022
# script untuk convert data dari hasil
# scrapping tabel ke excel
#--------------------------------------------

import requests
import pandas as pd
from bs4 import BeautifulSoup

alamat = "http://masukan_url_nya"
html = requests.get(alamat).text
data = BeautifulSoup(html, 'html.parser')

table = data.findAll("table", {"class":"table table-hover table-bordered general-table"})[0] 
rows = table.findAll("tr")
for row in rows:
	for cell in row.findAll(["td", "th"]):
		#print(cell.get_text())
		cell.get_text()
#Masukan data dalam tag td dan th ke dalam list
hasil = []
for row in rows:
	info = []
	for cell in row.findAll(["td", "th"]):
		info.append(cell.get_text())
	#print(hasil.append(info))
	hasil.append(info)

df = pd.DataFrame(hasil) #convert list hasil jadi dataframe
new_header = df.iloc[0] 
df = df[1:] 
#print(df)
df.columns = new_header # mengubah first row menjadi column header
df.reset_index(drop=True, inplace=True) #reset index sehingga dimulai dari 0

#filter value column
rslt_df = df.loc[df['nama kolom'] == 'value kolom']
#nama file
file_name = data.find('small').text
out = rslt_df.to_excel(r'/home/dy/nama_file'+file_name+'.xlsx', sheet_name='nama_sheet', index=False)


print(out)

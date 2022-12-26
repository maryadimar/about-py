#--------------------------------------------
# Dibuat oleh maryadi
# pada 26/12/2022
# script untuk mematikan PC
#--------------------------------------------

import os

shutdown = input("Mau shutdown Komputer ? (yes / no): ")

if shutdown == 'no':
	exit()
else:
	#untuk windows
	#os.system("shutdown /s /t 1")
	#untuk linux
	os.system("shutdown now -h")

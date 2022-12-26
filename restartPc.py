#--------------------------------------------
# Dibuat oleh maryadi
# pada 26/12/2022
# script untuk restart PC
#--------------------------------------------

import os

restart = input("Mau restart Komputer ? (yes / no): ")

if restart == 'no':
	exit()
else:
	#untuk windows
	#os.system("shutdown /r /t 1")
	#untuk linux
	os.system("shutdown -r now")

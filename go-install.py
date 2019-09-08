#/usr/bin/python
# -*- coding: utf-8 -*-
#Copyright 2019 GO-INSTALL
#Written by: Adrian Guillermo
#Facebook: Adrian Guillero
#Github: https://www.github.com/AdrMXR

class bcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    OCRA = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

import time
import os
from sys import exit 
from getch import pause  

os.system('clear')

def banner():
    bann= "\n\n"                                                  
    bann += "                   ____                          \n"
    bann += "                 / ___| ___                      \n"             
    bann += "                | |  _ / _ \                     \n"
    bann += "                | |_| | (_) |                    \n"
    bann += "         ___     \____|\___/    _ _              \n"
    bann += "        |_ _|_ __  ___| |_ __ _| | |             \n"
    bann += "         | || '_ \/ __| __/ _` | | |             \n"
    bann += "         | || | | \__ \ || (_| | | |             \n"
    bann += "        |___|_| |_|___/\__\__,_|_|_|             \n"
    bann += "                                   v1.0          \n"
    print(bcolors.RED + bcolors.BOLD + bann  + bcolors.ENDC + bcolors.ENDC).center(110)


def menu():
	print("   ---------------------------------------    ")
	print("  ||                 MENU                ||   ")
	print("   ---------------------------------------    ")
	print("  ||          [1] Instalar Go            ||   ")
	print("  ||           	                         ||   ")
	print("  || 	      [2] Actualizar Go          ||   ")
	print("  ||                                     ||   ")
	print("  ||          [3] Desinstalar Go         ||   ")
	print("   ---------------------------------------    ")

def actions():
	option = input("[*] Selecciona una opcion: ")
	if option == 1:
		os.system('cd /usr/local && sudo curl -O https://storage.googleapis.com/golang/go1.9.linux-amd64.tar.gz && sudo tar -xzvf go1.9.linux-amd64.tar.gz && echo export PATH=$PATH:/usr/local/go/bin >> /etc/profile')
		if raw_input("¿Desea crear una carpeta especifica de trabajo? (y/n)\n--> ").upper() != "Y":
			os.system('clear')
			print("\nGRACIAS POR UTILIZAR GO INSTALL, PARA COMPROBAR SU INSTALACION DE GO TECLEE GO VERSION EN SU TERMINAL." + bcolors.RED)
			exit(0)
		carpet = raw_input("Ingrese un nombre para su carpeta: ")
		time.sleep(3)
		os.system('cd $HOME && mkdir {}'.format(carpet))
		os.system('echo export GOPATH=$HOME/{} >> /etc/profile'.format(carpet))
		os.system('cd $HOME/{} && mkdir -p src/github.com'.format(carpet))
		print("PARA EFECTUAR LOS CAMBIOS, ES NECESARIO REINICIAR SU PC...")
		time.sleep(3)
		if raw_input("¿Desea reiniciar ahora su Pc? (y/n)\n--> ").upper() != "Y":
			os.system('clear')
			print("\nGRACIAS POR UTILIZAR GO INSTALL")
			exit(0)
		os.system('reboot')

	elif option == 2:
		directory = os.getcwd()
		print("Actualizando GO...")
		os.system('cd {0}/Defs/update-golang && ./update-golang.sh'.format(directory))
		time.sleep(3)
		pause("PARA EFECTUAR LOS CAMBIOS ES NECESARIO REINICIAR SU PC ...")
		time.sleep(2)
		if raw_input("¿Desea reiniciar ahora su Pc? (y/n)\n--> ").upper() != "Y":
			os.system('clear')
			print("\nGRACIAS POR UTILIZAR GO INSTALL")
			exit(0)
		os.system('reboot')


	elif option == 3:
		print("Removiendo GO...")
		os.system('rm -rf /usr/local/go')
		time.sleep(3)
		pause("GO removido, presione cualquier tecla para salir...")
		exit(0)

	else:
		return actions()

banner()
menu()
actions()

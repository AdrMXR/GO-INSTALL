<p align="center"><img src="https://miro.medium.com/max/3000/1*30aoNxlSnaYrLhBT0O1lzw.png" /></p>

## ¿Qué es Golang?
Go es un lenguaje de programación relacionado mucho con la syntaxis de C. Este lenguaje ha sido creado por el conglomerado que todos conocemos, Google. Sus principales virtudes son la simplicidad y la multifuncionalidad, aspectos que han perseguido sus autores desde el principio. El lenguaje desarrollado por Google contiene la facilidad de la programación de los lenguajes interpretados y dinámicos y la eficiencia y la seguridad de un lenguaje compilado de tipado estático (statically typed). A esto se añade que la estructura de Go obedece a la finalidad de acortar el proceso de desarrollo de modo que también permita crear en un solo ordenador grandes archivos ejecutables en poco tiempo. Algunas de las características distintivas con las cuales puede alcanzarse este nivel de calidad son las siguientes:

* Un sistema de tipos ligero pero expresivo que permite clasificar y diferenciar objetos (variables, funciones, etc.)
* Concurrencia (cálculos simultáneos), que permite una ejecución más rápida de los programas
* El recolector de basura para usar racionalmente la memoria y evitar problemas de espacio
* Una estricta especificación de dependencias sin una syntaxis de declaraciones compleja
* Multiplataforma, para usar las aplicaciones desarrolladas en cualquier sistema


## Acerca de GO INSTALL
GO-INSTALL se enfoca en la automatización. Esta consta de 3 opciones al ejecutar la herramienta:
* Instalar Go: Automaticamente se descargará de la pagina oficial de Golang la versión más reciente y comenzará su instalación y configuración. Al finalizar su instalación se le cuestionará si desea crear una carpeta especifica para sus proyectos, en caso de rechazar la petición sus proyectos se guardan en el directorio $HOME/go/src/github.com, en caso de aceptar, se creará una carpeta con su nombre deseado en el mismo directorio y se configurará el PATH en el archivo /etc/profile. Al final se le cuestiona si desea reiniciar su pc, es recomendable aceptar para efectuar los cambios correctamente. 
* Actualizar Go: En esta opción se ejecuta el script <a href="https://github.com/udhos/update-golang">update-golang</a> y determina que versión tiene instalada y si hay una versión disponible para instalar. Al final se le cuestiona si desea reiniciar su Pc, les recomiendo que acepten para efectuar los cambios. 
* Desinstalar Go: Simplemente se elimina el directorio de Go ubicado en /usr/local. Si usted anteriormente ha tenido problemas con su instalación de Go manualmente puede utilizar esta opción y posteriormente utilizar la opción 1 para restaurar su configuración de Go correctamente. 

## Instalación 
```bash
sudo apt install python2.7 python-pip  
```
```bash
git clone https://github.com/AdrMXR/GO-INSTALL.git
```
```bash
cd GO-INSTALL
```
```bash
pip install -r requirements.txt 
```
```bash
python go-install.py 
```


## Screenshot de la herramienta
<p align="center"><img src="https://github.com/AdrMXR/GO-INSTALL/blob/master/Screenshot.png" /></p>


## Creditos
Creador de la herramienta: Adrian Guillermo

Facebook: https://www.facebook.com/Adrian.Guillermo.22

Instagram: https://www.instagram.com/adrian.guillermo22/

YouTube: https://www.youtube.com/channel/UCqEtxJKbIghx6lyymrjfvnA?view_as=subscriber

































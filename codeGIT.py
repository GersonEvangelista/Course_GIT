git init #Para iniciar el proyecto
git status -s #Lista todos los archivos disponibles en el proyecto

git add #Pasa el file de directorio de trabajo al área de ensayo
git add archivo.txt #hace un seguimiento al archivo
git add . #Hacer seguimiento a todos los files

#Para deshacer la accion del "git add ."
git reset 

git commit -m "mensaje" #pasa el file del área de ensayo al repositorio local
git commit -am "mensaje" #Para hacer Add y commit al mismo tiempo solo cuando se ha modificado un archivo

#Para configurar usuario y correo 
git config --global user.username "Gerson"
git config --global user.email "gersonchaev@gmail.com"

#Para mostrar la lista de todos los commits
git log --oneline

#Para ir a la instantánea o versión (commit) que se quiera
#si aplicas esto se eliminaran los commits que le siguen
git reset --hard CODIGO_INSTANTÁNEO_DEL_GIT_LOG
git reset --hard 01cdac6

#Para moverse a un commit previo sin eliminar ningun commit
git checkout CODIGO_INSTANTÁNEO_DEL_GIT_LOG .
git checkout 01cdac6 .

#Para modificar el mensaje del commit
git commit --amend
:i ; esc ; suprimir ; esc ; :i ; "nuevo nombre" ; enter ; esc ; :wq

#Para subir archivos a gitHub
git push LINK_REPO #previamente debe existir el repo

#Para traer todos los cambios de remoto a local
git pull

#Para crear etiquetas "tag" que indican a GIT que se ha terminado una #versión 
git tag fecha_version -m "mensaje"
git tag 17-12-23 -m "mensaje"

#Para subir un "tag" o versión a GitHub
git push --tags

#Para clonar o recuperar un proyecto de gitHub 
git clone LINK_REPO

#Para crear una rama
git branch NAME
git branch #para ver las ramas y la rama donde te encuentras 
#cambiar a la rama NAME
git checkout NAME 
git switch NAME
NOTA: Lo que se hace en una rama no afecta lo que se hace en la otra.

#Para hacer merge
#1ero se va a la rama principal y luego se hace merge
git merge RAMA #Indica que se va hacer merge de rama principal con RAMA

#Para borrar una rama
git branch -d NOMBRE_RAMA

#Para borrar credenciales (cuando se cambia de cuenta en gitHub)
configuración, Cuentas, BuscarCredenciales, Adminitrados de credenciales, Credenciales de windows, BuscarGitYquitar.
#Nota: Luego de borrar las credenciales y aplicar push pedirá ingresar los nuevos credenciales

#Para compartir el proyecto y puedan editar varios (gitHub)
irAlproyecto, settings, collaborators, add people, username.

#LinkDocumentaciónGIT: https://git-scm.com/docs
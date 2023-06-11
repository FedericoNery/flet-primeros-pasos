# Configuración para desarrollar con flet
## PyCharm
### Pasos a seguir:

1. Crear un proyecto con entorno virtual (venv)
2. Abrir la terminal CMD. Si aparece (venv) por delante de la ruta en la que se encuentra la terminal
obviar el siguiente paso, sino:
3. Una vez creado el entorno virtual, acceder por medio de la terminal ejecutar:
```
cd venv
cd Scripts
activate.bat
```

4. Deberiamos visualizar en la pantalla de la terminal 
```
(venv) C:/rutas-directorios/.../
```

5. Instalar flet, poniendo el mouse por encima del package subrayado con rojo.

6. En la terminal de CMD, ejecutar el archivo donde tenemos nuestra aplicación: 
```
flet app.py -r -w
```

## VSCode
### Pasos a seguir:


1. Crear una carpeta nueva y abrirla con la opción OpenFolder de VsCode
2. Abrir la terminal, ya sea CMD o BASH. Donde se tenga configurado python.
Recomiendo CMD o BASH
3. Ejecutar el comando 
```
python -m venv venv
```
4. Una vez creado el entorno virtual, acceder por medio de la terminal ejecutar:
```
cd venv
cd Scripts
activate.bat
```

5. Deberiamos visualizar en la pantalla de la terminal 
```
(venv) C:/rutas-directorios/.../flet-pokedex
```

6. Preguntar por la versión de Python para corroborar con -> ```python --version```

7. Ahora ejecutar los siguientes comandos:
```
pip install pokebase
pip install flet
```

8. Ejecutar el siguiente comando, esto genera un archivo requirements.txt que es basicamente un archivo de dependencias/librerias, para que si nosotros queremos desarrollar en otra computadora o dispositivo, podemos reconstruir nuestro proyecto con exactamente la misma versión de librerias que utilizamos:
```
pip freeze
```

9. Ahora siempre estando conectado o vinculado al venv. Nuestro archivo app.py es el archivo principal donde tenemos el componente main de nuestra aplicación: 
```
flet app.py -r -w
```
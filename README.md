# Proyecto API Clientes

# Descripción

Este proyecto consiste en la creación de una API básica utilizando FastAPI.  
La API permite mostrar información de un proyecto y una lista de clientes mediante endpoints.

# Creación del proyecto

Primero se creó una carpeta llamada `nombre_pro_clientes` en el escritorio para posteriormente abrirla en Visual Studio Code.

# Creación del entorno virtual

Dentro de Visual Studio Code se abrió la terminal y se creó el entorno virtual con el siguiente comando:

py -m venv yober

Este comando crea un entorno virtual llamado `yober`, el cual permite trabajar con librerías independientes del sistema principal de Python.

# Activación del entorno virtual

Después de crear el entorno virtual, se activó utilizando el siguiente comando:

.\yober\Scripts\activate

Cuando el entorno virtual se activa correctamente, aparece el nombre `(yober)` al inicio de la terminal.

# Instalación de FastAPI

Luego se instaló el framework FastAPI con el siguiente comando:

pip install "fastapi[standard]"


Este comando instala FastAPI junto con sus dependencias necesarias para ejecutar la API.


# librerías instaladas

Después de la instalación se utilizó el siguiente comando para verificar las librerías instaladas:

pip list

Con este comando se confirmó que FastAPI estaba instalado correctamente.

# creacion archivo main.py

Después se creó el archivo principal llamado `main.py`, donde se desarrollaron los endpoints de la API.

Las primeras líneas escritas fueron:

from fastapi import FastAPI 

app = FastAPI()


## Explicación

 `from fastapi import FastAPI`  
  Importa la clase FastAPI necesaria para crear la aplicación.

 `app = FastAPI()`  
  Crea la aplicación principal de la API.
# Creación de endpoints


@app.get("/proyecto")

def mensaje():
    return {"proyecto": "este es el proyecto de clientes a desarrollar"}

### Explicación

Este endpoint crea una ruta llamada `/proyecto`.  
Cuando el usuario ingresa a esa ruta, la API devuelve un mensaje en formato JSON con información del proyecto.

## Endpoint de clientes

lista_clientes = ["Ricardo","yoberson","quiroga","daniela","ana","kamila","zuelima"]

@app.get("/clientes")
def clientes():
    return {"clientes": lista_clientes}


### Explicación

Este endpoint crea una ruta llamada `/clientes`.  
Al ingresar a esta ruta, la API muestra una lista de clientes almacenados dentro de una variable.

# Ejecución

Para ejecutar la API se utilizó el siguiente comando:

fastapi dev main.py

# Resultado

Al ejecutar el proyecto, la API queda disponible localmente en:

http://127.0.0.1:8000


Endpoints disponibles:

- `/proyecto`
- `/clientes`


# Proyecto Urban Grocers 

## Descripción

Este proyecto contiene pruebas automatizadas para la funcionalidad de creación de usuarios y kits de usuarios en la aplicación Urban Grocers.

## Tecnologías y Técnicas Utilizadas

- Lenguaje de Programación: Python
- Framework de Pruebas: pytest
- Librería de Solicitudes HTTP: requests

## Estructura del Proyecto
El proyecto contiene los siguientes archivos:

- Configuration.py: contiene las constantes de configuración, como la URL del servicio y las rutas de las API.
- Data.py: almacena los datos de prueba, como los encabezados y los cuerpos de solicitud.
- Sender_stand_request.py: contiene las funciones para enviar solicitudes HTTP a la API.
- Create_user_test.py: archivo que contiene las pruebas automatizadas para la funcionalidad de creación de usuarios. Se verifica que el campo "firstName" cumpla con los requisitos establecidos.
- Create_kit_name_kit_test.py: archivo que contiene las pruebas automatizadas para la funcionalidad de creación de kits de usuarios. Se verifica que el campo "name" cumpla con los requisitos establecidos.
- README.md: archivo que proporciona información general sobre el proyecto.
- Gitignore: archivo de configuración para excluir archivos y directorios innecesarios del control de versiones.

## Ejecución de las Pruebas
Antes de ejecutar las pruebas, asegurarse de tener instalados los siguientes paquetes de Python:

- Pytest
- Requests

Para ejecutar las pruebas, primero actualiza la constante que contiene la URL que se encuentra en el archivo configuration.py. Luego usa la terminal y ejecuta el comando "pytest" seguido del nombre del archivo que contiene las pruebas.

## Créditos

Ingrid Bernal Mechea, Cohorte 13.
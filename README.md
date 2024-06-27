# FastAPI - Api de predicción 

Proyecto de backend desarrollado en Python con el framework [FastAPI](https://fastapi.tiangolo.com/), para la creacion de una API RESTful que retorne la predicción de un modelo de machine learning basado en las características de entrada.

## Ejecutar el proyecto
Como **prerrequisito** es necesario tener instalado [Docker](https://docs.docker.com/engine/install/) en el sistema, la instalacion es bastante sencilla. Sin embargo aca hay un [link](https://www.youtube.com/watch?v=ZO4KWQfUBBc&ab_channel=FaztCode) por si llega a ser necesario.

Si el proyecto se esta viendo desde el repositorio de github, es necesario primero hacer estos pasos, si ya se encuentra en la carpeta raiz del proyecto,puede pasar directamente al paso 3.

1- Clonar el repositorio :

    git clone https://github.com/Nemesis1019/Prediction_API.git

2- Ir a la carpeta raiz del proyecto:

    cd Prediction_API

La carpeta del proyecto se debe ver asi :

![root_proyect](https://firebasestorage.googleapis.com/v0/b/portafolio-images.appspot.com/o/raiz.PNG?alt=media&token=69a4d92d-b811-487e-af91-8f5f17ecaf57)

3- Estando en la carpeta raiz del proyecto, primero es necesario crear la imagen de Docker a partir del Dockerfile:
    
    docker build -t prediction_api .

El nombre por defecto es prediction_api, sin embargo se puede cambiar por el de preferencia.

4- Lo siguiente es crear un contenedor a partir de la imagen que creamos anteriormente :

    docker run -d -p 8000:8000 --name container_api prediction_api
    
El nombre del contenedor en este caso es container_api, sin embargo tambien se puede cambiar a conveniencia.

Siguiendo correctamente los pasos anteriormente dichos, la aplicación debe estar en funcionamiento.

**Comandos que pueden ser de ayuda :**

-Listar las imagenes creadas:

    docker image ls
 
-Observar los logs dentro del contenedor:

    docker logs "nombre del contenedor"
 
 -Listar los contenedores que esten activos:
 
    docker ps
    
-Listar todos los contenedores:
    
    docker ps -a

## Documentacion

La API consta de 2 endpoints.

-El primero es una bienvenida a la API,el cual regresa un mensaje por defecto, se accede mediante la ruta por defecto **/**, es decir :

    http://localhost:8000/

![welcome](https://firebasestorage.googleapis.com/v0/b/portafolio-images.appspot.com/o/4.PNG?alt=media&token=23fc2eca-78ba-434c-bebf-1c208c233653)

**Ejemplos de funcionamiento :**

![welcome_example](https://firebasestorage.googleapis.com/v0/b/portafolio-images.appspot.com/o/7.PNG?alt=media&token=630e41f2-a10c-4750-8e81-4da7ad894bbb)


-El **SEGUNDO ENPOINT** es el que se pide especificamente en la prueba, "/predict" , es decir:

    http://localhost:8000/predict

![predict_example](https://firebasestorage.googleapis.com/v0/b/portafolio-images.appspot.com/o/1.PNG?alt=media&token=a2547551-d49f-463e-bdfd-c77fe91a5c4a)

La consulta http es de tipo POST, por lo que al momento de hacer la consulta es necesario enviarle un request body, que en este caso debe estar en formato JSON.

![Body_example](https://firebasestorage.googleapis.com/v0/b/portafolio-images.appspot.com/o/2.PNG?alt=media&token=6a93c30e-c233-49dc-852c-424170de4aea)

Los datos teben estar definidos tomando como ejemplo la imagen anterior.

**Ejemplos de funcionamiento :**

-Datos de entrada :

![entry_data](https://firebasestorage.googleapis.com/v0/b/portafolio-images.appspot.com/o/5.PNG?alt=media&token=f103e9c7-c0fc-4fe8-a832-61d08bcad2d9)

-Respuesta :

![response](https://firebasestorage.googleapis.com/v0/b/portafolio-images.appspot.com/o/6.PNG?alt=media&token=1ca93967-ee3a-4b7c-a800-35e01f192c6f)

Una vez desplegado el proyecto, también se puede acceder a la documentacion de la API en el siguiente enlace :  

http://localhost:8000/docs

## Entregables

El repositorio contiene todos lo que se pidio como entregable , en la carpeta services, se encuentra un script llamado train_model.py , que corresponde al entrenamiento del proyecto, la documentación está tanto en el README, como de manera online, esta también el dockerfile y los archivos de la api serian los restantes.

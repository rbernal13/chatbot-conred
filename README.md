# **chatbot-conred (backend)**

 <blockquote>
    <strong>Nota:</strong> Para Visual Studio Code, se recomienda instalar una extension que permita visualizar archivos MarkDown (.md) de forma local. Una recomendacion es instalar <strong>Markdown All in One by Yu Zhang</strong> para Visual Studio Code.
</blockquote>

## **Configuracion del entorno virtual (venv)**

Para ejecutar el back de forma local, la maquina u ordenador debe tener instalado **Python 3.9+** y debe configurar un entorno virtual para instalar las respectivas librerias y dependencias del proyecto. Para ello, abrimos una terminal sobre la raiz del proyecto (Ej: *github_repositorios/chatbot-conred*) y ejecutamos el siguiente comando:

```shell
py -3 -m venv venv
```

Esto genera una carpeta denominada **"venv"** en la cual estara localizado el entorno virtual. Una vez creado, **debe activar el entorno virtual** con siguiente comando:
```shell
venv/Scripts/activate
```
## **Dependencias y librerias**

A parte de usar Python 3.9+, el proyecto utiliza las siguiente dependencias:
- flask
- pyngrok
- pandas
- google_spreadsheet
- google-auth-oauthlib
- gspread-dataframe
- pydrive

Para instalar una libreria, se debe utilizar el siguiente comando (No olvidar activar el entorno virtual):
```shell
pip install <nombre-de-la-dependencia>
```
Ejemplo:

```shell
pip install flask
```

## **Ejecutar el proyecto de forma local**

Para ejecutar este proyecto, primero debe ejecutar la instancia de Flask:

```shell
flask --app server run
```

Esto ejecutara nuesto servidor por defecto en el puerto 5000

## **Conectar nuestro backend con Dialogflow**

Para conectar nuestro servidor de Flask con Dialogflow, debemos exponer nuestro servidor usando un tunel. Para ello usaremos en ngrok:

```shell
ngrok http 5000
```
Con esto, expondremos nuestro servidor en la web. Ahora debemos dirgirnos a Dialogflow -> Fulfillment y activar el Webhook. En el campo **URL** debemos copiar la url de tipo https generada por ngrok y posteriormente hacemos click en Save/Guardar. Dicha url debe tener un formato similar al mostrado a continuacion:
```
https://2832-181-53-12-151.ngrok.io
```

## Configuracion de las variables de entorno
Las variables de entorno deberan quedar configuradas en el archivo spredsheet-api-key.json
```variables
  "type": <type-account>,
  "project_id": <id-proyecto>,
  "private_key_id": <id-de-la-llave>,
  "private_key": <token-private-key>",
  "client_email": <correo-cliente-GCP-IAM>,
  "client_id": <id-del-correo-en-GCP-IAM>,
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/<url-correo-cliente-en-GCP-IAM>"
```

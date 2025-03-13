import json

from src.services.Google.spreadsheet import guardar_datos


def encuesta_despedida(req: json):
    
    # Sacar de contextos los datos que se necesitan accediendo al JSON

    nombre = req["queryResult"]["outputContexts"][2]["parameters"]["nombre.original"]
    email = req["queryResult"]["outputContexts"][2]["parameters"]["email.original"]    
    respuesta0 = req["queryResult"]["outputContexts"][0]["parameters"]["respuesta0.original"]
    respuesta1 = req["queryResult"]["outputContexts"][0]["parameters"]["respuesta1.original"]
    respuesta2 = req["queryResult"]["outputContexts"][0]["parameters"]["respuesta2.original"]
    respuesta3 = req["queryResult"]["outputContexts"][0]["parameters"]["respuesta3.original"]

    #Uso de funcion para guardar los datos y enviarlos al google spreadsheet
    guardar_datos(nombre,email,respuesta0,respuesta1,respuesta2,respuesta3)

    # fullfillment
    res = {
        "fulfillmentMessages": [
            {"text": {"text": [
                "Gracias por utilizar nuestro canal de atención, te invitamos a conocer mas de nuestra comunidad CONRED en la página www.conred.co y canal telefónico 018000180848"]}},
        ],
    }
    return res

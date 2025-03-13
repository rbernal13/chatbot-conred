import json

from src.services.Google.spreadsheet import guardar_datos


def encuesta_satisfaccion(req: json):
    
    # Obtener respuesta del usuario de la anterior intencion e imprimir en consola
    respuesta = req.get('queryResult').get('queryText')
    print(respuesta)

    # fullfillment
    res = {
        "fulfillmentMessages": [
            {"text": {"text": [
                "Para nosotros es importante conocer tu opinion para que tu experiencia sea cada vez mejor, a continuación, por favor cuéntanos como te fue con la atención que te acabamos de brindar \n ¿Tu inquietud  o requerimiento fue resuelto?"]}},
            {
                "payload": {
                    "richContent": [
                        [
                            {
                                "type": "chips",
                                "options": [
                                    {
                                        "text": "Si"
                                    },
                                    {
                                        "text": "No"
                                    }
                                ]
                            }
                        ]
                    ]
                }
            },
        ],
    }
    return res

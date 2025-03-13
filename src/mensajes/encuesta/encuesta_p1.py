import json

from src.services.Google.spreadsheet import guardar_datos


def encuesta_pregunta1(req: json):

    # Obtener respuesta del usuario de la anterior intencion e imprimir en consola
    respuesta1 = req.get('queryResult').get('queryText')
    print(respuesta1)

    # fullfillment.
    res = {
        "fulfillmentMessages": [
            {"text": {"text": [
                "En una escala de 1 a 5, donde 1 es muy insatisfecho y 5 muy satisfecho ¿Qué tan satisfecho te encuentras con el servicio brindado en este canal?"]}},
            {
                "payload": {
                    "richContent": [
                        [
                            {
                                "type": "chips",
                                "options": [
                                    {
                                        "text": "1"
                                    },
                                    {
                                        "text": "2"
                                    },
                                    {
                                        "text": "3"
                                    },
                                    {
                                        "text": "4"
                                    },
                                    {
                                        "text": "5"
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

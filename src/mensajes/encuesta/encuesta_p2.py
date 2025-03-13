import json

from src.services.Google.spreadsheet import guardar_datos


def encuesta_pregunta2(req: json):

    # Obtener respuesta del usuario de la anterior intencion e imprimir en consola
    respuesta2 = req.get('queryResult').get('queryText')
    print(respuesta2)

    # fullfillment
    res = {
        "fulfillmentMessages": [
            {"text": {"text": [
                "¿Qué tan fácil ha sido gestionar tu solicitud o requerimiento a través de este canal?"]}},
            {
                "payload": {
                    "richContent": [
                        [
                            {
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
                                ],
                                "type": "chips"
                            }
                        ]
                    ]
                }
            },
        ],
    }
    return res

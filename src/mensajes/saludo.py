def saludo(req):           
    res = {
        "fulfillmentMessages": [
            {"text": {"text": [
                "Hola soy XXXX tu asistente virtual de CONRED. Recuerda que haciendo uso de mi servicio, aceptas los términos y condiciones y las políticas de tratamiento de datos personales de CONRED que puedes consultar haciendo click en el siguiente link: \n https://www.conred.co/carvajal/es/#/home/conred/app1/inicio/1"]}},
            {
                "payload": {
                    "richContent": [
                        [
                            {
                                "type": "chips",
                                "options": [
                                    {
                                        "text": "Acepto"
                                    },
                                    {
                                        "text": "No Acepto"
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
